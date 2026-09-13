import argparse
import sys
from core.ingest import IngestionManager
from core.llm_client import LLMClient
from core.evaluator import StudentProjectEvaluator

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Student Project Capability & Ceiling CLI")
    parser.add_argument("--test", action="store_true", help="Run automated self-test on sample source")
    parser.add_argument("--ceiling", action="store_true", help="Probe maximum project tier from sources")
    parser.add_argument("--challenge", type=str, help="Challenge student to build a specific project")
    parser.add_argument("--add-url", type=str, help="Ingest a web URL as source curriculum")
    parser.add_argument("--list", action="store_true", help="List all ingested sources")

    args = parser.parse_args()
    ingest_mgr = IngestionManager()
    evaluator = StudentProjectEvaluator(ingest_manager=ingest_mgr)

    if args.add_url:
        print(f"Fetching URL: {args.add_url}...")
        res = ingest_mgr.fetch_url(args.add_url)
        print(f"Saved: {res['filename']} ({res['length']} chars)")
        return

    if args.list:
        sources = ingest_mgr.list_sources()
        print(f"\n--- Ingested Sources ({len(sources)}) ---")
        for s in sources:
            print(f"- {s['filename']}: {s['title']} ({s['size_bytes']} bytes)")
        return

    if args.ceiling or args.test:
        print("\n--- Running Virtual Student Ceiling Probe ---")
        res = evaluator.probe_curriculum_ceiling()
        if res["success"]:
            print(res["report"])
        else:
            print("Error:", res["error"])
        return

    if args.challenge:
        print(f"\n--- Challenging Student to Build: '{args.challenge}' ---")
        res = evaluator.challenge_project(args.challenge)
        if res["success"]:
            print(res["report"])
        else:
            print("Error:", res["error"])
        return

    parser.print_help()

if __name__ == "__main__":
    main()
