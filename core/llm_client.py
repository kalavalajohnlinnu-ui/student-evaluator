import os
import json
import re
from typing import Optional, Dict, Any
import requests

class LLMClient:
    """Pluggable LLM caller supporting Gemini API, OpenAI-compatible APIs, Local Ollama/LMStudio, and Offline Simulation."""

    def __init__(self, api_key: Optional[str] = None, provider: str = "auto", model: Optional[str] = None, endpoint: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or os.environ.get("OPENAI_API_KEY")
        self.provider = provider
        self.model = model
        self.endpoint = endpoint or os.environ.get("LOCAL_LLM_ENDPOINT")

        # Auto-detect provider if not specified
        if self.provider == "auto":
            if os.environ.get("OLLAMA_HOST") or self.endpoint:
                self.provider = "ollama"
            elif os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
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
            elif self.provider == "ollama":
                self.model = "qwen2.5-coder:7b"
            else:
                self.model = "offline-mock"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """Generate response from configured provider or offline mock engine."""
        if self.provider == "mock" and not self.endpoint:
            return self._mock_student_evaluation(system_prompt, user_prompt)

        try:
            if self.provider == "ollama":
                return self._call_ollama(system_prompt, user_prompt)
            elif self.provider == "gemini":
                return self._call_gemini(system_prompt, user_prompt)
            elif self.provider == "openai":
                return self._call_openai(system_prompt, user_prompt)
            elif self.provider == "local":
                return self._call_openai_compatible(system_prompt, user_prompt)
            else:
                return self._mock_student_evaluation(system_prompt, user_prompt)
        except Exception as e:
            return (
                f"> [!WARNING]\n> Local/Remote API call failed ({str(e)}). Running internal Offline Simulator.\n\n"
                + self._mock_student_evaluation(system_prompt, user_prompt)
            )

    def _call_ollama(self, system_prompt: str, user_prompt: str) -> str:
        base_url = self.endpoint or "http://localhost:11434"
        url = f"{base_url.rstrip('/')}/api/generate"
        payload = {
            "model": self.model,
            "prompt": f"System Instructions:\n{system_prompt}\n\nTask:\n{user_prompt}",
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json().get("response", "")

    def _call_openai_compatible(self, system_prompt: str, user_prompt: str) -> str:
        base_url = self.endpoint or "http://localhost:1234/v1"
        url = f"{base_url.rstrip('/')}/chat/completions"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

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
                "maxOutputTokens": 3000
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
        """Intelligent offline evaluator when no local or remote LLM endpoint is active."""
        is_ceiling_probe = "Curriculum Concept Inventory" in user_prompt
        is_problem_solve = "STUDENT PROBLEM-SOLVING TASK:" in user_prompt

        # Mode 1: Problem Solver & Builder Mode
        if is_problem_solve:
            prob_match = re.search(r'STUDENT PROBLEM-SOLVING TASK:\s*"(.*?)"', user_prompt, re.DOTALL)
            problem = prob_match.group(1).strip() if prob_match else "Problem"

            forbidden = []
            for kw in ["pandas", "numpy", "react", "vue", "angular", "flask", "fastapi", "django", "express", "axios", "spring", "docker", "bootstrap"]:
                if kw in problem.lower():
                    forbidden.append(kw)

            forbidden_msg = ""
            if forbidden:
                forbidden_msg = (
                    "\n> [!CAUTION]\n"
                    f"> **Forbidden / Outside Technology Requested**: `{', '.join(forbidden)}`\n"
                    "> The student explicitly refuses to use this library because it was **NEVER taught** on CodeHero. "
                    "The solution below uses **pure native syntax** from your curriculum instead.\n"
                )

            is_sql = any(k in problem.lower() for k in ["sql", "table", "select", "database", "query"])
            is_web = any(k in problem.lower() for k in ["html", "css", "dom", "button", "website", "card", "flexbox"])

            if is_sql:
                return (
                    f"# 💡 Student Grounded Solution: \"{problem}\"\n"
                    f"{forbidden_msg}\n"
                    "### 1. Curriculum Reference Check\n"
                    "- **Realm**: 🗝️ SQL\n"
                    "- **Modules Used**: `[SQL Module 1: Tables & Data]`, `[SQL Module 3: Filtering & WHERE]`, `[SQL Module 6: Aggregations & GROUP BY]`\n\n"
                    "### 2. Feasibility with CodeHero Knowledge\n"
                    "- **Status**: **100% FEASIBLE**\n"
                    "- **Student Assessment**: Can be solved entirely using standard SQL queries taught in your platform.\n\n"
                    "### 3. Strictly Grounded Solution Code\n"
                    "```sql\n"
                    "-- Solution written exclusively using CodeHero SQL syntax\n"
                    "CREATE TABLE IF NOT EXISTS records (\n"
                    "    id INTEGER PRIMARY KEY,\n"
                    "    name TEXT NOT NULL,\n"
                    "    category TEXT,\n"
                    "    value NUMERIC\n"
                    ");\n\n"
                    "-- Query using taught WHERE and GROUP BY\n"
                    "SELECT category, COUNT(*) AS total_items, AVG(value) AS average_value\n"
                    "FROM records\n"
                    "WHERE value > 0\n"
                    "GROUP BY category\n"
                    "ORDER BY total_items DESC;\n"
                    "```\n\n"
                    "### 4. Step-by-Step Explanation as a Student\n"
                    "\"I created the table using the `CREATE TABLE` syntax taught in Module 1, and grouped the data using `GROUP BY` and aggregate functions (`COUNT`, `AVG`) taught in Module 6.\"\n"
                )

            elif is_web:
                return (
                    f"# 💡 Student Grounded Solution: \"{problem}\"\n"
                    f"{forbidden_msg}\n"
                    "### 1. Curriculum Reference Check\n"
                    "- **Realms**: 🎨 HTML & CSS + ⚡ JavaScript\n"
                    "- **Modules Used**: `[HTML/CSS Module 7: Flexbox]`, `[HTML/CSS Module 12: Forms & Inputs]`, `[JavaScript Module 4: DOM Events]`, `[JavaScript Module 19: LocalStorage]`\n\n"
                    "### 2. Feasibility with CodeHero Knowledge\n"
                    "- **Status**: **100% FEASIBLE**\n"
                    "- **Student Assessment**: Built entirely within client-side browser capabilities taught on CodeHero.\n\n"
                    "### 3. Strictly Grounded Solution Code\n"
                    "```html\n"
                    "<div class=\"card-container\" style=\"display: flex; flex-direction: column; gap: 12px; padding: 16px; border: 1px solid #ccc; border-radius: 8px;\">\n"
                    "  <h3>Interactive Component</h3>\n"
                    "  <input type=\"text\" id=\"userInput\" placeholder=\"Enter text...\" style=\"padding: 8px; border-radius: 4px; border: 1px solid #ddd;\" />\n"
                    "  <button id=\"submitBtn\" style=\"padding: 8px 16px; background: #4f46e5; color: white; border: none; border-radius: 4px; cursor: pointer;\">Execute Action</button>\n"
                    "  <div id=\"outputArea\" style=\"margin-top: 8px; font-weight: 500;\"></div>\n"
                    "</div>\n\n"
                    "<script>\n"
                    "  // Strictly using taught CodeHero JS events and LocalStorage\n"
                    "  const btn = document.getElementById(\"submitBtn\");\n"
                    "  const input = document.getElementById(\"userInput\");\n"
                    "  const output = document.getElementById(\"outputArea\");\n\n"
                    "  // Load saved state from LocalStorage (taught in Module 19)\n"
                    "  const saved = localStorage.getItem(\"codehero_demo_state\");\n"
                    "  if (saved) output.innerText = \"Loaded: \" + saved;\n\n"
                    "  btn.addEventListener(\"click\", function() {\n"
                    "    const val = input.value.trim();\n"
                    "    if (val) {\n"
                    "      output.innerText = \"Result: \" + val;\n"
                    "      localStorage.setItem(\"codehero_demo_state\", val);\n"
                    "      input.value = \"\";\n"
                    "    }\n"
                    "  });\n"
                    "</script>\n"
                    "```\n\n"
                    "### 4. Step-by-Step Explanation as a Student\n"
                    "\"I used CSS Flexbox (taught in Module 7) for modern vertical alignment, attached a click event with `addEventListener` (taught in Module 4), and saved the input state using `localStorage.setItem` (taught in Module 19) so it persists when the page reloads.\"\n"
                )

            # Default: Python
            return (
                f"# 💡 Student Grounded Solution: \"{problem}\"\n"
                f"{forbidden_msg}\n"
                "### 1. Curriculum Reference Check\n"
                "- **Realm**: 🐍 Python\n"
                "- **Modules Used**: \n"
                "  - `[Python Module 4: Repetition & Loops]`\n"
                "  - `[Python Module 7: Functions & Modular Code]`\n"
                "  - `[Python Module 8: Error Handling]`\n"
                "  - `[Python Module 18: File I/O & Serialization (JSON/CSV)]`\n\n"
                "### 2. Feasibility with CodeHero Knowledge\n"
                "- **Status**: **100% FEASIBLE**\n"
                "- **Student Assessment**: Solved purely using Python core built-ins and standard file handling taught on your site.\n\n"
                "### 3. Strictly Grounded Solution Code\n"
                "```python\n"
                "# Solution crafted strictly with CodeHero Python syntax\n"
                "import json\n\n"
                "def solve_task(data_list, filename=\"solution_output.json\"):\n"
                "    \"\"\"\n"
                "    Uses functions (Module 7), error handling (Module 8), \n"
                "    and File I/O with JSON (Module 18).\n"
                "    \"\"\"\n"
                "    results = []\n"
                "    for idx, item in enumerate(data_list, start=1):\n"
                "        try:\n"
                "            entry = {\"id\": idx, \"value\": item, \"active\": True}\n"
                "            results.append(entry)\n"
                "        except Exception as e:\n"
                "            print(\"[Error processing item]:\", e)\n\n"
                "    try:\n"
                "        with open(filename, \"w\", encoding=\"utf-8\") as f:\n"
                "            json.dump(results, f, indent=2)\n"
                "        print(f\"Saved {len(results)} records to '{filename}'\")\n"
                "    except IOError as err:\n"
                "        print(\"File error:\", err)\n\n"
                "    return results\n\n"
                "if __name__ == \"__main__\":\n"
                "    test_data = [\"Apple\", \"Banana\", \"Cherry\"]\n"
                "    output = solve_task(test_data)\n"
                "    print(\"Generated records:\", output)\n"
                "```\n\n"
                "### 4. Step-by-Step Explanation as a Student\n"
                "\"I created a modular function with parameters and return values (Module 7), iterated through the input using a `for` loop (Module 4), protected against unexpected issues using `try/except` (Module 8), and saved the final output to disk using `open()` with `json.dump()` (Module 18).\"\n"
            )

        # Mode 2: Ceiling Probe
        if is_ceiling_probe:
            return """# 🎓 Virtual Student Ceiling Assessment: CodeHero Universe (1717)

> **Source Platform**: [https://kalavalajohnlinnu-ui.github.io/codehero-1717/](https://kalavalajohnlinnu-ui.github.io/codehero-1717/)  
> **Student Constraint**: 100% Closed-Book. Zero outside programming knowledge.

---

### 1. Curriculum Concept Inventory Across 6 Realms

Based **exclusively** on your website's 141 modules and 539 lessons, the student has acquired the following capabilities:

| Realm | Concepts Mastered From Site | Depth Level |
| :--- | :--- | :--- |
| 🐍 **Python** | Variables, Control Flow, Lists/Tuples/Dicts/Sets, Functions, OOP, Error Handling, Decorators, Generators, File I/O (JSON/CSV), Regex, Asyncio Concurrency | **Advanced Core (Tier 3)** |
| ⚡ **JavaScript** | DOM Manipulation, Event Handling, ES6+ (Arrow functions, Destructuring), LocalStorage, Promises, Async/Await, Canvas basics | **Interactive Client-Side (Tier 2/3)** |
| 🎨 **HTML & CSS** | Semantic tags, Forms, Tables, Flexbox, CSS Grid, Media Queries, Keyframe Animations, Transitions | **Responsive Frontend (Tier 2)** |
| 🗝️ **SQL** | Tables, `SELECT`, `WHERE`, `JOIN` (INNER/LEFT/RIGHT), `GROUP BY`, Aggregates, Transactions, Indexes | **Relational Querying (Tier 2/3)** |
| ☕ **Java** | Types, OOP (Classes, Interfaces, Polymorphism), Generics, Collections Framework, Multithreading, Streams | **Object-Oriented Architecture (Tier 3)** |
| 🦀 **Rust** | Ownership & Borrowing, Lifetimes, Structs & Enums, Pattern Matching, Traits, Error Handling (`Result`/`Option`) | **Systems Fundamentals (Tier 3)** |

---

### 2. Highest Achievable Project Tier

#### 🏆 **Tier 3: Advanced Standalone & Data-Driven Applications (Achieved!)**
Students who complete your website's tracks can build sophisticated, standalone software systems in each language.

#### Examples of Projects Students CAN Build Right Now:
1. **Python**:
   - Automated Expense Tracker with JSON/CSV file persistence.
   - CLI RPG Game with OOP character classes and inventory system.
   - Multi-threaded or asynchronous web log analyzer.
2. **JavaScript + HTML/CSS**:
   - Complete Interactive To-Do List with `localStorage` persistence.
   - Dynamic Quiz Game with timers, audio feedback, and scoreboards.
   - Filterable E-Commerce Product Catalog (client-side state).
3. **SQL**:
   - Complete Relational School/Store Database schema with normalization and analytics reports.
4. **Java**:
   - Console Banking Application with transaction logs and multithreading.
5. **Rust**:
   - High-performance memory-safe text indexer and CLI grep tool.

---

### 3. The "Curriculum Ceiling" (Where Students Hit a Wall)

#### ⚠️ **The Integration Gap (Full-Stack Ceiling):**
While your website provides exceptional depth in **individual languages**, a student cannot build a **Full-Stack Web Application** (e.g., React frontend + Python FastAPI/Flask backend + PostgreSQL database) using only your website.

**The 3 Missing Bridge Concepts:**
1. **The Python/SQL Bridge**: The curriculum teaches Python (Modules 1-25) and SQL (Modules 1-20), but does **not** teach database connectors (like `sqlite3`, `psycopg2`, or SQLAlchemy) inside Python.
2. **The Web Server / Backend Bridge**: Python is taught as a CLI language. Server frameworks (like `Flask`, `FastAPI`, or `Django`) and Node.js (`Express`) are not yet included.
3. **Authentication & Deployment**: User login sessions (JWT / cookies) and hosting/deployment (Docker, cloud servers) are not covered.
"""

        # Mode 3: Project Challenge Response for CodeHero
        project_name = "Target Project"
        proj_match = re.search(r'TARGET PROJECT TO BUILD:\s*"(.*?)"', user_prompt)
        if proj_match:
            project_name = proj_match.group(1)

        safe_cls = re.sub(r'[^a-zA-Z0-9]', '', project_name) or 'ProjectApp'
        safe_file = re.sub(r'[^a-zA-Z0-9_]', '_', project_name).lower()

        return (
            f"# 🛠️ Student Project Challenge Attempt: \"{project_name}\"\n\n"
            f"> **Platform Tested**: [https://kalavalajohnlinnu-ui.github.io/codehero-1717/](https://kalavalajohnlinnu-ui.github.io/codehero-1717/)  \n"
            f"> **Student Condition**: Trained exclusively on CodeHero's 539 lessons.\n\n"
            "---\n\n"
            "### 1. Feasibility Assessment\n"
            "- **Status**: **HIGHLY FEASIBLE (Client-Side / CLI) | PARTIALLY FEASIBLE (Full-Stack)**\n"
            "- **Confidence**: 85%\n"
            "- **Evaluation**: \n"
            f"  - If \"{project_name}\" is built as an in-browser web app (HTML + CSS + JS) or a Python desktop application, the student **HAS ALL the prerequisites** from your site (File I/O, OOP, DOM events, and state management).\n"
            f"  - If \"{project_name}\" requires a live client-server network with user login and cloud databases, the student will hit an **Integration Blocker**.\n\n"
            "---\n\n"
            "### 2. Available Building Blocks Used From CodeHero\n"
            "- **Logic & Control Flow**: Modules 1-7 (Loops, Conditionals, Functions).\n"
            "- **Data Architecture**: Module 9 & 15 (OOP Classes & Encapsulation).\n"
            "- **Persistence**: Python Module 18 (`json.dump` / file write) or JS Module 19 (`localStorage`).\n"
            "- **UI & Interaction**: HTML/CSS Flexbox + JavaScript Event Listeners.\n\n"
            "---\n\n"
            "### 3. Knowledge Blockers (If Targeted as Full-Stack)\n"
            "- 🔴 **Missing Backend Route**: CodeHero does not teach HTTP server routing (`Flask` or `FastAPI` in Python, or `Express` in JS).\n"
            "- 🔴 **Missing DB Driver**: CodeHero teaches raw SQL queries, but does not teach how to run SQL queries inside a Python script or JS backend.\n\n"
            "---\n\n"
            "### 4. Implementation Code (Strictly Grounded in CodeHero Content)\n"
            "```python\n"
            "# Student implementation using ONLY taught CodeHero Python concepts (OOP + File I/O)\n"
            "import json\n\n"
            f"class {safe_cls}:\n"
            f"    def __init__(self, filename=\"{safe_file}_data.json\"):\n"
            "        self.filename = filename\n"
            "        self.data = self.load_data()\n\n"
            "    def load_data(self):\n"
            "        try:\n"
            "            with open(self.filename, 'r', encoding='utf-8') as f:\n"
            "                return json.load(f)\n"
            "        except (FileNotFoundError, json.JSONDecodeError):\n"
            "            return []\n\n"
            "    def save_data(self):\n"
            "        with open(self.filename, 'w', encoding='utf-8') as f:\n"
            "            json.dump(self.data, f, indent=2)\n\n"
            "    def add_entry(self, item_name, details):\n"
            "        entry = {\"id\": len(self.data) + 1, \"name\": item_name, \"details\": details}\n"
            "        self.data.append(entry)\n"
            "        self.save_data()\n"
            "        print(f\"[OK] Added: {item_name}\")\n\n"
            "    def list_all(self):\n"
            f"        print(f\"\\n--- {project_name} Records ---\")\n"
            "        for item in self.data:\n"
            "            print(f\" #{item['id']} - {item['name']}: {item['details']}\")\n\n"
            "if __name__ == \"__main__\":\n"
            f"    app = {safe_cls}()\n"
            "    app.add_entry(\"Sample Entry\", \"Created using CodeHero Module 9 OOP & Module 18 File I/O\")\n"
            "    app.list_all()\n"
            "```\n\n"
            "---\n\n"
            "### 5. Curriculum Recommendations to Reach Tier 4 (Production)\n"
            "To take your students from Tier 3 to Tier 4, consider adding a **\"Bridge Realm\"**:\n"
            "1. **Python + SQLite Bridge**: 1 short module on `import sqlite3` so students can connect their Python code to their SQL database.\n"
            "2. **Minimal API Server**: 1 module introducing `FastAPI` or `Flask` so students can connect their HTML/JS frontends to their Python logic.\n"
        )
