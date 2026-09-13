# 🎓 Student Project Capability & Curriculum Ceiling Evaluator

A test harness for educational platforms and learning apps. It treats an AI model as a **strictly closed-book student** whose entire world of technical knowledge is restricted to your website's content.

With this tool, you can:
1. **Find your Curriculum Ceiling**: Discover the absolute highest project tier (Tier 1–4) a student can build with 100% self-sufficiency.
2. **Challenge Specific Projects**: Test whether a student can build a specific project (e.g. "To-Do List", "Weather App", "E-Commerce Cart").
3. **Detect Knowledge Blockers**: Pinpoint the exact missing concepts preventing students from building higher-tier projects.

---

## 📁 Project Structure

```
student-evaluator/
│
├── data/
│   └── sources/             <-- Put your web content or lessons here (*.md, *.txt)
│       └── sample_lesson.md <-- Included sample lesson placeholder
│
├── core/
│   ├── ingest.py            <-- Web scraper & text ingestion manager
│   ├── sandbox.py           <-- Strict closed-book prompt engineering
│   ├── llm_client.py        <-- Gemini / OpenAI caller + Offline Mock engine
│   └── evaluator.py         <-- Ceiling probe & project challenge runner
│
├── static/
│   └── index.html           <-- Modern interactive web dashboard
│
├── app.py                   <-- FastAPI web application
├── run.py                   <-- One-click launcher (`python run.py`)
├── cli.py                   <-- Terminal CLI runner (`python cli.py`)
├── .env.example             <-- API keys configuration template
└── README.md
```

---

## 🚀 Quick Start

### 1. Launch the Web Dashboard
```bash
python run.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

### 2. Ingest Your Website Details
In the dashboard (or via CLI):
- **Web URL**: Enter your live website URL (e.g., `https://your-learning-app.com/lesson-1`) and click **Fetch & Ingest Page**.
- **Paste Text**: Paste raw lesson text or tutorial markdown directly.

### 3. Run Evaluations
- **Run Ceiling Probe 🚀**: Discovers the highest achievable project tier and lists the top 3 missing concepts.
- **Challenge Student 🎯**: Enter a project name (e.g., *"Interactive Quiz App"*) to see how the student attempts it and where they get blocked.

---

## 💻 CLI Commands

You can also run evaluations directly in your terminal:

```bash
# List all active curriculum sources
python cli.py --list

# Ingest a live web page
python cli.py --add-url https://example.com/tutorial

# Probe curriculum ceiling
python cli.py --ceiling

# Challenge a specific project
python cli.py --challenge "E-Commerce Shopping Cart"

# Run self-test
python cli.py --test
```

---

## 🔑 LLM API Configuration (Optional)
The system includes an **Offline Mock Simulation Engine** that works out of the box with zero setup.

To connect live models:
1. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. Either enter it in the web dashboard under **Settings**, or set it in your environment:
   ```bash
   set GEMINI_API_KEY=your_key_here
   ```
