from typing import Dict, Any, Optional
from core.ingest import IngestionManager
from core.sandbox import (
    STUDENT_SYSTEM_PROMPT,
    CEILING_PROBE_PROMPT,
    PROJECT_CHALLENGE_PROMPT
)
from core.llm_client import LLMClient

class StudentProjectEvaluator:
    """Evaluates the project-building capability of a strictly grounded student model."""

    def __init__(self, ingest_manager: Optional[IngestionManager] = None, llm_client: Optional[LLMClient] = None):
        self.ingest = ingest_manager or IngestionManager()
        self.llm = llm_client or LLMClient()

    def probe_curriculum_ceiling(self) -> Dict[str, Any]:
        """Probes the maximum achievable project tier based on the current saved sources."""
        curriculum = self.ingest.get_combined_curriculum()
        if not curriculum.strip():
            return {
                "success": False,
                "error": "No curriculum sources found! Please add web URLs or lesson text first.",
                "report": ""
            }

        system_instruction = STUDENT_SYSTEM_PROMPT.format(curriculum=curriculum)
        user_prompt = CEILING_PROBE_PROMPT

        report = self.llm.generate(system_instruction, user_prompt)
        return {
            "success": True,
            "curriculum_length": len(curriculum),
            "sources_count": len(self.ingest.list_sources()),
            "report": report
        }

    def challenge_project(self, project_name: str, project_description: str = "") -> Dict[str, Any]:
        """Challenges the student to design and build a specific project solely with taught concepts."""
        curriculum = self.ingest.get_combined_curriculum()
        if not curriculum.strip():
            return {
                "success": False,
                "error": "No curriculum sources found! Please add web URLs or lesson text first.",
                "report": ""
            }

        system_instruction = STUDENT_SYSTEM_PROMPT.format(curriculum=curriculum)
        user_prompt = PROJECT_CHALLENGE_PROMPT.format(
            project_name=project_name,
            project_description=project_description or "Build a fully working implementation of this project."
        )

        report = self.llm.generate(system_instruction, user_prompt)
        return {
            "success": True,
            "project_name": project_name,
            "report": report
        }
