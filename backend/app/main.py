from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes_repo import router as repo_router

app = FastAPI(
    title="Devscribe GitHub Info Backend",
    version="0.1.0",
)

# Allow frontend (for CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(repo_router, prefix="/api/repo", tags=["repo"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
