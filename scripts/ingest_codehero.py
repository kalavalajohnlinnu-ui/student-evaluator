import sys
import json
import requests
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


BASE_DIR = Path(__file__).resolve().parent.parent
SOURCES_DIR = BASE_DIR / "data" / "sources"
SOURCES_DIR.mkdir(parents=True, exist_ok=True)

# Clean out existing markdown files in sources
for f in SOURCES_DIR.glob("*.md"):
    f.unlink()

BASE_URL = "https://raw.githubusercontent.com/kalavalajohnlinnu-ui/codehero-1717/main/src/data"

LANGUAGES = [
    {"name": "Python", "file": "curriculum.json", "is_root": True},
    {"name": "JavaScript", "file": "languages/javascript.json", "is_root": False},
    {"name": "HTML & CSS", "file": "languages/html.json", "is_root": False},
    {"name": "SQL", "file": "languages/sql.json", "is_root": False},
    {"name": "Java", "file": "languages/java.json", "is_root": False},
    {"name": "Rust", "file": "languages/rust.json", "is_root": False},
]

total_modules = 0
total_lessons = 0

for lang in LANGUAGES:
    url = f"{BASE_URL}/{lang['file']}"
    print(f"Fetching {lang['name']} from {url}...")
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"Failed to fetch {lang['name']}: {e}")
        continue

    lang_lessons = 0
    lang_slug = lang["name"].lower().replace(" & ", "_").replace(" ", "_")

    for idx, module in enumerate(data, start=1):
        total_modules += 1
        mod_id = module.get("id", f"{lang_slug}-mod-{idx}")
        title = module.get("title", f"Module {idx}")
        desc = module.get("description", "")
        lessons = module.get("lessons", [])
        total_lessons += len(lessons)
        lang_lessons += len(lessons)

        lines = [
            f"# [{lang['name'].upper()}] {title}",
            f"**Description**: {desc}\n",
            f"**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/\n",
            f"**Language Realm**: {lang['name']}\n",
            "## Lessons & Concepts Covered:\n"
        ]

        for l_idx, lesson in enumerate(lessons, start=1):
            l_title = lesson.get("title", f"Lesson {l_idx}")
            l_badge = lesson.get("badge", "")
            concept = lesson.get("concept", "")
            starter = lesson.get("starterCode", "")
            solution = lesson.get("solution", "")

            lines.append(f"### {l_title} [{l_badge}]")
            if concept:
                lines.append(concept)
            if starter:
                lines.append(f"\n**Code Example / Starter**:\n```{lang_slug}\n{starter}\n```")
            if solution and solution != starter:
                lines.append(f"\n**Solution Pattern**:\n```{lang_slug}\n{solution}\n```")
            lines.append("\n---\n")

        mod_filename = f"{lang_slug}_mod_{idx:02d}.md"
        (SOURCES_DIR / mod_filename).write_text("\n".join(lines), encoding="utf-8")

    print(f"✓ Saved {lang['name']}: {len(data)} modules, {lang_lessons} lessons.")

# Fetch projects catalog
print("Fetching projects catalog...")
proj_url = f"{BASE_URL}/projects/projects.json"
try:
    proj_resp = requests.get(proj_url, timeout=30)
    proj_resp.raise_for_status()
    projects_data = proj_resp.json()

    proj_lines = [
        "# CodeHero Curriculum Projects Catalog",
        "**Platform Source**: https://kalavalajohnlinnu-ui.github.io/codehero-1717/\n",
        "Target hands-on student projects defined in the CodeHero platform:\n"
    ]

    for p in projects_data:
        p_title = p.get("title", "Project")
        p_lang = p.get("language", "general")
        p_diff = p.get("difficulty", "beginner")
        p_desc = p.get("description", "")
        steps = p.get("steps", [])
        proj_lines.append(f"## {p_title} ({p_lang.upper()} - {p_diff.upper()})")
        proj_lines.append(f"**Description**: {p_desc}")
        proj_lines.append(f"**Steps Count**: {len(steps)}")
        for s in steps:
            proj_lines.append(f"- Step {s.get('stepNumber')}: {s.get('title', '')} - {s.get('description', '')}")
        proj_lines.append("\n---\n")

    (SOURCES_DIR / "codehero_projects_catalog.md").write_text("\n".join(proj_lines), encoding="utf-8")
    print(f"✓ Saved Projects Catalog: {len(projects_data)} projects.")
except Exception as e:
    print(f"Failed to fetch projects: {e}")

print("\n🎉 Comprehensive Ingestion Complete!")
print(f"Total Modules Ingested: {total_modules}")
print(f"Total Lessons Ingested: {total_lessons}")
print(f"Destination: {SOURCES_DIR}")
