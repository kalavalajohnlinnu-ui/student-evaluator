import os
import re
from pathlib import Path
from typing import List, Dict, Optional
from html.parser import HTMLParser
import requests

SOURCES_DIR = Path(__file__).resolve().parent.parent / "data" / "sources"

class SimpleTextExtractor(HTMLParser):
    """Clean HTML to plain text without needing heavy external dependencies."""
    def __init__(self):
        super().__init__()
        self.text_parts: List[str] = []
        self.ignore_tags = {"script", "style", "head", "meta", "noscript", "svg"}
        self._current_tag = None

    def handle_starttag(self, tag, attrs):
        self._current_tag = tag.lower()
        if self._current_tag in {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "div", "br"}:
            self.text_parts.append("\n")

    def handle_endtag(self, tag):
        self._current_tag = None
        if tag.lower() in {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "div"}:
            self.text_parts.append("\n")

    def handle_data(self, data):
        if self._current_tag not in self.ignore_tags:
            cleaned = data.strip()
            if cleaned:
                self.text_parts.append(cleaned + " ")

    def get_text(self) -> str:
        raw = "".join(self.text_parts)
        # Normalize consecutive whitespace / newlines
        cleaned = re.sub(r"\n\s*\n+", "\n\n", raw)
        return cleaned.strip()


class IngestionManager:
    """Manages curriculum ingestion from web URLs, raw text, or files."""

    def __init__(self, sources_dir: Path = SOURCES_DIR):
        self.sources_dir = sources_dir
        self.sources_dir.mkdir(parents=True, exist_ok=True)

    def fetch_url(self, url: str, title: Optional[str] = None) -> Dict[str, str]:
        """Fetch content from a web URL, convert HTML to clean markdown-like text, and save it."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()

        parser = SimpleTextExtractor()
        parser.feed(resp.text)
        content = parser.get_text()

        # Generate a slug/filename
        safe_title = title or re.sub(r"[^\w\-_]", "_", url.replace("https://", "").replace("http://", ""))
        safe_title = safe_title[:50].strip("_")
        filename = f"{safe_title}.md"
        file_path = self.sources_dir / filename

        file_content = f"# Source: {url}\n\n{content}"
        file_path.write_text(file_content, encoding="utf-8")

        return {
            "title": safe_title,
            "filename": filename,
            "path": str(file_path),
            "content": file_content,
            "length": len(file_content)
        }

    def save_raw_lesson(self, title: str, content: str) -> Dict[str, str]:
        """Save a lesson pasted as text or markdown directly."""
        safe_title = re.sub(r"[^\w\-_]", "_", title).strip("_") or "lesson"
        filename = f"{safe_title}.md"
        file_path = self.sources_dir / filename

        file_path.write_text(content, encoding="utf-8")
        return {
            "title": safe_title,
            "filename": filename,
            "path": str(file_path),
            "content": content,
            "length": len(content)
        }

    def list_sources(self) -> List[Dict[str, str]]:
        """List all saved curriculum files."""
        items = []
        for file in sorted(self.sources_dir.glob("*.md")):
            text = file.read_text(encoding="utf-8", errors="ignore")
            first_line = text.split("\n")[0].strip("# ") if text else file.stem
            items.append({
                "filename": file.name,
                "title": first_line or file.stem,
                "path": str(file),
                "size_bytes": file.stat().st_size,
                "preview": text[:200] + ("..." if len(text) > 200 else "")
            })
        return items

    def get_combined_curriculum(self) -> str:
        """Combine all saved sources into one comprehensive curriculum context."""
        sources = self.list_sources()
        if not sources:
            return ""

        combined = []
        for s in sources:
            file_path = Path(s["path"])
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            combined.append(f"=== MODULE: {s['filename']} ===\n{text}\n")
        return "\n\n".join(combined)

    def clear_all(self):
        """Remove all saved sources."""
        for file in self.sources_dir.glob("*.md"):
            try:
                file.unlink()
            except Exception:
                pass
