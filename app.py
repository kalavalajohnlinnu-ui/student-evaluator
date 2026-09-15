import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

from core.ingest import IngestionManager
from core.llm_client import LLMClient
from core.evaluator import StudentProjectEvaluator

app = FastAPI(title="Student Project Capability Evaluator")

# State & Managers
ingest_mgr = IngestionManager()
llm_cli = LLMClient()
evaluator = StudentProjectEvaluator(ingest_manager=ingest_mgr, llm_client=llm_cli)

STATIC_DIR = Path(__file__).resolve().parent / "static"

# Request Schemas
class IngestUrlRequest(BaseModel):
    url: str
    title: Optional[str] = None

class IngestTextRequest(BaseModel):
    title: str
    content: str

class ChallengeRequest(BaseModel):
    project_name: str
    project_description: Optional[str] = ""

class SolveProblemRequest(BaseModel):
    problem_statement: str
    target_language: Optional[str] = "auto"

class SettingsRequest(BaseModel):
    api_key: Optional[str] = None
    provider: Optional[str] = "mock"
    model: Optional[str] = None
    endpoint: Optional[str] = None


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        raise HTTPException(status_code=404, detail="index.html not found")
    return index_file.read_text(encoding="utf-8")


@app.get("/api/sources")
async def list_sources():
    sources = ingest_mgr.list_sources()
    return {"success": True, "sources": sources}


@app.post("/api/sources/url")
async def ingest_url(req: IngestUrlRequest):
    try:
        result = ingest_mgr.fetch_url(req.url, title=req.title)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.post("/api/sources/text")
async def ingest_text(req: IngestTextRequest):
    try:
        result = ingest_mgr.save_raw_lesson(req.title, req.content)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.delete("/api/sources/{filename}")
async def delete_source(filename: str):
    target = ingest_mgr.sources_dir / filename
    if target.exists():
        target.unlink()
        return {"success": True, "deleted": filename}
    return {"success": False, "error": "File not found"}


@app.post("/api/evaluate/ceiling")
async def evaluate_ceiling():
    res = evaluator.probe_curriculum_ceiling()
    return res


@app.post("/api/evaluate/challenge")
async def evaluate_challenge(req: ChallengeRequest):
    res = evaluator.challenge_project(req.project_name, req.project_description)
    return res


@app.post("/api/evaluate/solve")
async def evaluate_solve(req: SolveProblemRequest):
    res = evaluator.solve_problem(req.problem_statement, req.target_language)
    return res


@app.post("/api/settings")
async def update_settings(req: SettingsRequest):
    global llm_cli, evaluator
    llm_cli = LLMClient(
        api_key=req.api_key,
        provider=req.provider or "mock",
        model=req.model,
        endpoint=req.endpoint
    )
    evaluator = StudentProjectEvaluator(ingest_manager=ingest_mgr, llm_client=llm_cli)
    return {
        "success": True,
        "provider": llm_cli.provider,
        "model": llm_cli.model,
        "endpoint": llm_cli.endpoint
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
