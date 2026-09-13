import os
import json
import re
from typing import Optional, Dict, Any
import requests

class LLMClient:
    """Pluggable LLM caller supporting Gemini API, OpenAI-compatible APIs, and an intelligent Offline Mock mode."""

    def __init__(self, api_key: Optional[str] = None, provider: str = "auto", model: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or os.environ.get("OPENAI_API_KEY")
        self.provider = provider
        self.model = model

        # Auto-detect provider if not specified
        if self.provider == "auto":
            if os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
                self.provider = "gemini"
            elif os.environ.get("OPENAI_API_KEY"):
                self.provider = "openai"
            else:
                self.provider = "mock"

        if not self.model:
            if self.provider == "gemini":
                self.model = "gemini-2.5-flash"
            elif self.provider == "openai":
                self.model = "gpt-4o-mini"
            else:
                self.model = "offline-mock"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """Generate response from configured provider or offline mock engine."""
        if not self.api_key or self.provider == "mock":
            return self._mock_student_evaluation(system_prompt, user_prompt)

        try:
            if self.provider == "gemini":
                return self._call_gemini(system_prompt, user_prompt)
            elif self.provider == "openai":
                return self._call_openai(system_prompt, user_prompt)
            else:
                return self._mock_student_evaluation(system_prompt, user_prompt)
        except Exception as e:
            # Graceful fallback with warning
            return (
                f"> [!WARNING]\n> Direct API call failed ({str(e)}). Falling back to Offline Simulation.\n\n"
                + self._mock_student_evaluation(system_prompt, user_prompt)
            )

    def _call_gemini(self, system_prompt: str, user_prompt: str) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": f"System Instructions:\n{system_prompt}\n\nStudent Evaluation Task:\n{user_prompt}"}]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 2048
            }
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=45)
        resp.raise_for_status()
        data = resp.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    def _call_openai(self, system_prompt: str, user_prompt: str) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=45)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]

    def _mock_student_evaluation(self, system_prompt: str, user_prompt: str) -> str:
        """Intelligent offline evaluator when no API key is configured."""
        is_ceiling_probe = "Curriculum Concept Inventory" in user_prompt

        # Extract whatever concepts are mentioned in the curriculum text
        curr_match = re.search(r"CURRICULUM:\s*-+\s*(.*?)\s*-+", system_prompt, re.DOTALL)
        curriculum_text = curr_match.group(1) if curr_match else system_prompt

        tags = re.findall(r"`<(\w+)>`", curriculum_text)
        js_methods = re.findall(r"`([a-zA-Z0-9_\.]+)\(\)`", curriculum_text)

        tags_str = ", ".join(set(tags)) if tags else "Basic HTML elements"
        js_str = ", ".join(set(js_methods)) if js_methods else "Basic variables & click events"

        if is_ceiling_probe:
            return f"""# 🎓 Virtual Student Ceiling Assessment (Offline Simulation Mode)

> [!NOTE]
> *Simulated using deterministic rule-engine because no live LLM API key is configured.*
> *Set `GEMINI_API_KEY` in `.env` or in the settings tab to run live reasoning models.*

### 1. Curriculum Concept Inventory
Based exclusively on your supplied materials, the student currently knows:
- **HTML Tags**: {tags_str}
- **JavaScript & Logic**: {js_str}
- **Explicit Knowledge Exclusions**: No CSS layout (Flexbox/Grid), no backend/databases, no `fetch()` or persistence.

---

### 2. Highest Achievable Project Tier
**Tier 2: Interactive Standalone Client-Side App (Limited)**
The student can build interactive single-page mini-apps where state lives in memory (until refreshed). They CANNOT build Tier 3 (Full-Stack) or Tier 4 (Authenticated) apps because server routes and persistent databases have not been introduced.

---

### 3. Flagship Capstone Project
**"Interactive Button Counter / Simple Clicker Game"**
- **Architecture**: A single `.html` file with an `<h1>`, an `<input>`, and `<button>` elements.
- **Features**: User types their name or clicks a button, and JavaScript changes the `innerText` of a target element.
- **Limitation**: As soon as the page is reloaded, all data is reset.

---

### 4. Immediate Knowledge Ceilings (Top 3 Missing Concepts)
1. **Data Persistence (`localStorage` / Databases)**: Students cannot build to-do lists, notes apps, or shopping carts that survive page refreshes.
2. **CSS Layout (Flexbox & Grid)**: Students can write elements, but cannot arrange them into modern responsive card grids or sidebars.
3. **HTTP Requests (`fetch` / REST APIs)**: Students cannot fetch live data (e.g., weather, news, external services).
"""

        # Otherwise, project challenge
        project_name = "Target Project"
        proj_match = re.search(r'TARGET PROJECT TO BUILD:\s*"(.*?)"', user_prompt)
        if proj_match:
            project_name = proj_match.group(1)

        return f"""# 🛠️ Student Project Challenge Attempt: "{project_name}" (Offline Simulation Mode)

### 1. Feasibility Assessment
- **Status**: **PARTIALLY FEASIBLE**
- **Confidence**: 40%
- **Explanation**: A student can assemble the visible input fields and button triggers using taught tags ({tags_str}), but critical architecture requirements for "{project_name}" are missing from the current curriculum.

### 2. Available Building Blocks Used
- Elements: {tags_str}
- Handlers: {js_str}

### 3. Knowledge Blockers (Where the Student Hits a Wall)
- 🔴 **Blocker 1: Data Persistence**: This project requires saving state, but storage systems (`localStorage`, SQL/NoSQL databases) have not been taught on your site.
- 🔴 **Blocker 2: Asynchronous Operations / Networking**: Cannot fetch or post data to a server.
- 🔴 **Blocker 3: Modern Layout & Responsive Design**: Only raw unstyled HTML elements can be rendered.

### 4. Code Implementation (Strictly Grounded)
```html
<!-- Student attempt: Only using taught elements -->
<div>
  <h1>{project_name}</h1>
  <input type="text" id="userInput" placeholder="Enter input...">
  <button id="actionBtn">Submit</button>
  <p id="outputDisplay">Result will appear here</p>
</div>

<script>
  // Strictly using document.getElementById and innerText
  const btn = document.getElementById("actionBtn");
  const display = document.getElementById("outputDisplay");

  btn.addEventListener("click", function() {{
    display.innerText = "Updated by student action!";
    /* BLOCKED: Cannot save data or connect to server - concept not in curriculum */
  }});
</script>
```

### 5. Curriculum Upgrade Recommendation
To enable students to build "{project_name}", add lessons covering:
1. **State Persistence**: Introduce `localStorage.setItem` and `localStorage.getItem`.
2. **Dynamic DOM Generation**: How to create and append list items dynamically.
3. **CSS Layout Foundations**: Basic flexbox container properties.
"""
