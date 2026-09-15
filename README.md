# 🎓 Student Capability & Project Ceiling Evaluator — CodeHero Universe (1717)

A closed-book evaluation harness for testing educational platforms and learning apps. It treats an AI model as a **strictly grounded student** whose entire universe of technical knowledge is restricted to your website's content: [**CodeHero Universe (1717)**](https://kalavalajohnlinnu-ui.github.io/codehero-1717/).

---

## 🌟 Connected Source Curriculum
- **Source Website**: [https://kalavalajohnlinnu-ui.github.io/codehero-1717/](https://kalavalajohnlinnu-ui.github.io/codehero-1717/)
- **Total Ingested Modules**: 141 modules
- **Total Ingested Lessons**: 539 lessons
- **Built-in Projects**: 15 projects
- **Language Realms**: 🐍 Python (25 modules), ⚡ JavaScript (25 modules), 🎨 HTML & CSS (22 modules), 🗝️ SQL (20 modules), ☕ Java (25 modules), 🦀 Rust (24 modules)
- **Database**: SQLite 3 with Full-Text Search (`lessons_fts` FTS5) in `data/curriculum_knowledge.db`

---

## 🚀 Key Capabilities

1. **Interactive Problem Solver & Builder (Strictly Grounded)**:
   - Tell the student to solve any problem or build a new feature.
   - Automatically searches the 539 indexed lessons in SQLite, quotes the exact modules used, and writes clean code strictly adhering to your curriculum.
   - **Active Guardrails**: If you request external libraries (e.g. `pandas`, `react`, `flask`, `docker`), the student **explicitly refuses** and solves the task using pure native syntax from your website instead.

2. **Curriculum Ceiling Probe**:
   - Discovers the absolute highest project tier achievable across each language realm (Tier 1–4).
   - Identifies the exact "Missing Bridges" needed to reach production full-stack capability.

3. **Target Project Challenge**:
   - Tests whether a student can build a specific project (e.g., *"E-Commerce Cart"* or *"Interactive Note App"*) and logs knowledge blockers.

4. **100% Offline Execution**:
   - **Mode A (Built-in)**: Zero setup, runs completely offline right inside Python using the local SQLite knowledge engine.
   - **Mode B (Local AI)**: Seamlessly connects to local runners like [Ollama](https://ollama.com) (`http://localhost:11434`) for offline generative AI on your CPU/GPU.

---

## 📁 Project Structure

```
student-evaluator/
│
├── data/
│   ├── curriculum_knowledge.db  <-- SQLite database with FTS5 index (539 lessons, 15 projects)
│   └── sources/                 <-- 141 Markdown curriculum module files
│
├── core/
│   ├── indexer.py               <-- SQLite FTS5 database builder & search engine
│   ├── resolver.py              <-- Semantic knowledge connector & guardrails
│   ├── sandbox.py               <-- Closed-book prompt constraints (zero outside knowledge)
│   ├── llm_client.py            <-- Offline simulator + Ollama/Gemini connectors
│   ├── evaluator.py             <-- Ceiling probe & project challenge runner
│   └── ingest.py                <-- Web URL & text ingestion manager
│
├── scripts/
│   ├── ingest_codehero.py       <-- Ingests all 6 languages from codehero-1717
│   └── evaluate_codehero.py     <-- Curriculum analysis helper
│
├── static/
│   └── index.html               <-- Interactive web dashboard with Problem Solver
│
├── app.py                       <-- FastAPI backend & REST API
├── cli.py                       <-- Terminal CLI runner with --solve, --ceiling, --challenge
├── run.py                       <-- One-click dashboard launcher
└── README.md
```

---

## 💻 How to Use

### 1. Web Dashboard (Visual)
```bash
python run.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser:
- Use the **Interactive Problem Solver & Builder** to test any task.
- Run the **Curriculum Ceiling Probe** to inspect project tiers.
- Switch between **Internal Offline**, **Local Ollama**, or **Gemini Cloud** in Settings.

### 2. Terminal CLI (PowerShell / Bash)
```bash
# Ask the student to solve a Python problem:
python cli.py --solve "Build a student grade tracker that saves data to a JSON file" --lang python

# Ask the student to solve an SQL problem:
python cli.py --solve "Write a query to group records and calculate average score" --lang sql

# Ask the student to build an interactive web component:
python cli.py --solve "Create an interactive card that saves user notes to local storage" --lang html

# Probe curriculum ceiling:
python cli.py --ceiling

# Challenge a specific project:
python cli.py --challenge "Shopping Cart App"
```
