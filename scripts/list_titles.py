import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core.ingest import IngestionManager

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

mgr = IngestionManager()
for i, s in enumerate(mgr.list_sources(), 1):
    print(f"{i}. {s['title']}")
