import sys
import uvicorn

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


if __name__ == "__main__":
    print("=" * 60)
    print("🎓 Student Capability & Project Ceiling Evaluator")
    print("🌐 Dashboard URL: http://localhost:8000")
    print("=" * 60)
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
