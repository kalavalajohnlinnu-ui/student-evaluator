import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core.ingest import IngestionManager

def run_codehero_audit():
    mgr = IngestionManager()
    sources = mgr.list_sources()

    languages = {
        "python": {"name": "Python", "files": [], "lessons": 0},
        "javascript": {"name": "JavaScript", "files": [], "lessons": 0},
        "html_css": {"name": "HTML & CSS", "files": [], "lessons": 0},
        "sql": {"name": "SQL", "files": [], "lessons": 0},
        "java": {"name": "Java", "files": [], "lessons": 0},
        "rust": {"name": "Rust", "files": [], "lessons": 0},
    }

    for s in sources:
        fn = s["filename"]
        for key in languages:
            if fn.startswith(key):
                languages[key]["files"].append(s)

    report_lines = []
    report_lines.append("# 🎓 Virtual Student Project Capability Report: CodeHero (1717)")
    report_lines.append("**Source Platform**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/")
    report_lines.append(f"**Total Modules Evaluated**: {len(sources) - 1}")
    report_lines.append("**Constraint**: Strictly Grounded — Student has ZERO prior knowledge outside this website.\n")
    report_lines.append("---\n")

    return languages

if __name__ == "__main__":
    langs = run_codehero_audit()
    print("Found language tracks:", {k: len(v["files"]) for k, v in langs.items()})
