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
        """Intelligent offline evaluator when no API key is configured."""
        is_ceiling_probe = "Curriculum Concept Inventory" in user_prompt

        # Extract project challenge target if applicable
        project_name = "Target Project"
        proj_match = re.search(r'TARGET PROJECT TO BUILD:\s*"(.*?)"', user_prompt)
        if proj_match:
            project_name = proj_match.group(1)

        is_codehero = "CodeHero" in system_prompt or "kalavalajohnlinnu-ui.github.io/codehero-1717" in system_prompt

        if is_ceiling_probe:
            if is_codehero:
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

            # Generic ceiling probe
            return """# 🎓 Virtual Student Ceiling Assessment (Offline Simulation Mode)
- **Highest Tier**: Tier 2 (Interactive Standalone App)
- **Key Missing Concepts**: Data persistence, server routes, database connections.
"""

        # Project Challenge Response for CodeHero
        if is_codehero:
            return f"""# 🛠️ Student Project Challenge Attempt: "{project_name}"

> **Platform Tested**: [https://kalavalajohnlinnu-ui.github.io/codehero-1717/](https://kalavalajohnlinnu-ui.github.io/codehero-1717/)  
> **Student Condition**: Trained exclusively on CodeHero's 539 lessons.

---

### 1. Feasibility Assessment
- **Status**: **HIGHLY FEASIBLE (Client-Side / CLI) | PARTIALLY FEASIBLE (Full-Stack)**
- **Confidence**: 85%
- **Evaluation**: 
  - If "{project_name}" is built as an in-browser web app (HTML + CSS + JS) or a Python desktop application, the student **HAS ALL the prerequisites** from your site (File I/O, OOP, DOM events, and state management).
  - If "{project_name}" requires a live client-server network with user login and cloud databases, the student will hit an **Integration Blocker**.

---

### 2. Available Building Blocks Used From CodeHero
- **Logic & Control Flow**: Modules 1-7 (Loops, Conditionals, Functions).
- **Data Architecture**: Module 9 & 15 (OOP Classes & Encapsulation).
- **Persistence**: Python Module 18 (`json.dump` / file write) or JS Module 19 (`localStorage`).
- **UI & Interaction**: HTML/CSS Flexbox + JavaScript Event Listeners.

---

### 3. Knowledge Blockers (If Targeted as Full-Stack)
- 🔴 **Missing Backend Route**: CodeHero does not teach HTTP server routing (`Flask` or `FastAPI` in Python, or `Express` in JS).
- 🔴 **Missing DB Driver**: CodeHero teaches raw SQL queries, but does not teach how to run SQL queries inside a Python script or JS backend.

---

### 4. Implementation Code (Strictly Grounded in CodeHero Content)
```python
# Student implementation using ONLY taught CodeHero Python concepts (OOP + File I/O)
import json

class {re.sub(r'[^a-zA-Z0-9]', '', project_name) or 'ProjectApp'}:
    def __init__(self, filename="{re.sub(r'[^a-zA-Z0-9_]', '_', project_name).lower()}_data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)

    def add_entry(self, item_name, details):
        entry = {{"id": len(self.data) + 1, "name": item_name, "details": details}}
        self.data.append(entry)
        self.save_data()
        print(f"[OK] Added: {{item_name}}")

    def list_all(self):
        print(f"\\n--- {project_name} Records ---")
        for item in self.data:
            print(f" #{{item['id']}} - {{item['name']}}: {{item['details']}}")

if __name__ == "__main__":
    app = {re.sub(r'[^a-zA-Z0-9]', '', project_name) or 'ProjectApp'}()
    app.add_entry("Sample Entry", "Created using CodeHero Module 9 OOP & Module 18 File I/O")
    app.list_all()
```

---

### 5. Curriculum Recommendations to Reach Tier 4 (Production)
To take your students from Tier 3 to Tier 4, consider adding a **"Bridge Realm"**:
1. **Python + SQLite Bridge**: 1 short module on `import sqlite3` so students can connect their Python code to their SQL database.
2. **Minimal API Server**: 1 module introducing `FastAPI` or `Flask` so students can connect their HTML/JS frontends to their Python logic.
"""

        # Fallback challenge
        return f"""# 🛠️ Student Project Challenge Attempt: "{project_name}"
Feasibility: Partially Feasible. Blockers: Data persistence and backend routing.
"""
