import re
import json
import httpx
from pathlib import Path
from fastapi import HTTPException

from app.core.config import settings

GITHUB_API_BASE = "https://api.github.com"
CACHE_PATH = Path("repo_cache.json")


def parse_github_url(url: str) -> tuple[str, str]:
    """Extract owner/repo from a GitHub URL."""
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)", url)
    if not m:
        raise HTTPException(status_code=400, detail="Invalid GitHub URL")

    owner = m.group(1)
    repo = m.group(2).removesuffix(".git").strip("/")
    return owner, repo


async def _get(path: str):
    """Internal helper for GitHub API requests."""
    headers = {"Accept": "application/vnd.github+json"}
    if settings.github_token:
        headers["Authorization"] = f"Bearer {settings.github_token}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(GITHUB_API_BASE + path, headers=headers)

    if resp.status_code != 200:
        raise HTTPException(
            status_code=resp.status_code,
            detail=f"GitHub API error: {resp.status_code} {resp.text}",
        )

    return resp.json()


async def fetch_repo_basic(owner: str, repo: str) -> dict:
    """Fetch core repository info from GitHub."""
    data = await _get(f"/repos/{owner}/{repo}")
    return {
        "name": data.get("name"),
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "html_url": data.get("html_url"),
        "default_branch": data.get("default_branch"),
        "language": data.get("language"),
        "topics": data.get("topics", []),
        "stargazers_count": data.get("stargazers_count", 0),
        "forks_count": data.get("forks_count", 0),
        "open_issues_count": data.get("open_issues_count", 0),
    }


async def fetch_repo_tree(owner: str, repo: str, max_items: int = 100) -> list[str]:
    """Fetch file tree for the repo."""
    tree_json = await _get(f"/repos/{owner}/{repo}/git/trees/HEAD?recursive=1")
    paths = [item["path"] for item in tree_json.get("tree", [])]
    return paths[:max_items]


# 🧾 Optional: simple local cache (saves fetched data)
def save_repo_data(owner: str, repo: str, data: dict):
    """Save fetched repo data locally to a JSON cache."""
    cache = {}
    if CACHE_PATH.exists():
        try:
            cache = json.loads(CACHE_PATH.read_text())
        except json.JSONDecodeError:
            cache = {}

    cache[f"{owner}/{repo}"] = data
    CACHE_PATH.write_text(json.dumps(cache, indent=2))
