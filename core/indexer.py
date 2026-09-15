import os
import sys
import json
import sqlite3
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "curriculum_knowledge.db"

class CurriculumIndexer:
    """Connects and indexes all lessons, code snippets, and projects into a structured SQLite knowledge base."""

    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Main lessons table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                id TEXT PRIMARY KEY,
                language TEXT,
                module_id TEXT,
                module_title TEXT,
                lesson_title TEXT,
                badge TEXT,
                concept_markdown TEXT,
                starter_code TEXT,
                solution_code TEXT,
                keywords TEXT
            )
            """)

            # Projects table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id TEXT PRIMARY KEY,
                title TEXT,
                language TEXT,
                difficulty TEXT,
                description TEXT,
                steps_json TEXT
            )
            """)

            # Full-Text Search (FTS5) table for instant offline semantic lookup
            cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS lessons_fts USING fts5(
                lesson_id UNINDEXED,
                language,
                module_title,
                lesson_title,
                concept_markdown,
                keywords,
                tokenize = 'porter unicode61'
            )
            """)
            conn.commit()

    def index_all_sources(self):
        """Fetches from CodeHero source endpoints and indexes every lesson and project."""
        import requests

        BASE_URL = "https://raw.githubusercontent.com/kalavalajohnlinnu-ui/codehero-1717/main/src/data"
        LANGUAGES = [
            {"name": "python", "label": "Python", "file": "curriculum.json"},
            {"name": "javascript", "label": "JavaScript", "file": "languages/javascript.json"},
            {"name": "html_css", "label": "HTML & CSS", "file": "languages/html.json"},
            {"name": "sql", "label": "SQL", "file": "languages/sql.json"},
            {"name": "java", "label": "Java", "file": "languages/java.json"},
            {"name": "rust", "label": "Rust", "file": "languages/rust.json"},
        ]

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM lessons")
            cursor.execute("DELETE FROM projects")
            cursor.execute("DELETE FROM lessons_fts")

            total_indexed = 0

            for lang in LANGUAGES:
                url = f"{BASE_URL}/{lang['file']}"
                try:
                    resp = requests.get(url, timeout=30)
                    resp.raise_for_status()
                    modules = resp.json()
                except Exception as e:
                    print(f"Error downloading {lang['label']}: {e}")
                    continue

                for m_idx, mod in enumerate(modules, 1):
                    mod_id = mod.get("id", f"{lang['name']}-mod-{m_idx}")
                    mod_title = mod.get("title", f"Module {m_idx}")
                    for l_idx, lesson in enumerate(mod.get("lessons", []), 1):
                        lesson_id = lesson.get("id", f"{mod_id}-l-{l_idx}")
                        l_title = lesson.get("title", f"Lesson {l_idx}")
                        badge = lesson.get("badge", "")
                        concept = lesson.get("concept", "")
                        starter = lesson.get("starterCode", "")
                        solution = lesson.get("solution", "")

                        # Extract code keywords and terms
                        terms = re.findall(r"`([^`]+)`", concept)
                        keywords_str = " ".join(set(terms))

                        cursor.execute("""
                        INSERT OR REPLACE INTO lessons 
                        (id, language, module_id, module_title, lesson_title, badge, concept_markdown, starter_code, solution_code, keywords)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (lesson_id, lang["name"], mod_id, mod_title, l_title, badge, concept, starter, solution, keywords_str))

                        cursor.execute("""
                        INSERT INTO lessons_fts (lesson_id, language, module_title, lesson_title, concept_markdown, keywords)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """, (lesson_id, lang["name"], mod_title, l_title, concept, keywords_str))

                        total_indexed += 1

            # Index Projects
            try:
                proj_resp = requests.get(f"{BASE_URL}/projects/projects.json", timeout=30)
                proj_resp.raise_for_status()
                for p in proj_resp.json():
                    cursor.execute("""
                    INSERT OR REPLACE INTO projects (id, title, language, difficulty, description, steps_json)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        p.get("id", ""),
                        p.get("title", "Project"),
                        p.get("language", "general"),
                        p.get("difficulty", "beginner"),
                        p.get("description", ""),
                        json.dumps(p.get("steps", []))
                    ))
            except Exception as e:
                print(f"Error downloading projects: {e}")

            conn.commit()
            print(f"✓ Connected and indexed {total_indexed} lessons and {cursor.execute('SELECT COUNT(*) FROM projects').fetchone()[0]} projects into SQLite database.")

    def search(self, query: str, language: str = None, limit: int = 5):
        """Full-Text Search for concepts matching any problem or keyword query."""
        clean_q = re.sub(r"[^\w\s]", " ", query).strip()
        if not clean_q:
            clean_q = "basics"

        # Split into keywords for FTS match
        tokens = [t for t in clean_q.split() if len(t) > 2]
        fts_query = " OR ".join(tokens[:8]) if tokens else clean_q

        with self.get_connection() as conn:
            cursor = conn.cursor()
            if language and language != "auto":
                sql = """
                SELECT l.*, rank FROM lessons_fts 
                JOIN lessons l ON l.id = lessons_fts.lesson_id
                WHERE lessons_fts MATCH ? AND l.language = ?
                ORDER BY rank
                LIMIT ?
                """
                cursor.execute(sql, (fts_query, language, limit))
            else:
                sql = """
                SELECT l.*, rank FROM lessons_fts 
                JOIN lessons l ON l.id = lessons_fts.lesson_id
                WHERE lessons_fts MATCH ?
                ORDER BY rank
                LIMIT ?
                """
                cursor.execute(sql, (fts_query, limit))

            rows = cursor.fetchall()
            return [dict(r) for r in rows]

if __name__ == "__main__":
    indexer = CurriculumIndexer()
    indexer.index_all_sources()
