from fastapi import APIRouter
from app.models.schemas import RepoInfoRequest, RepoInfoResponse
from app.services.github_service import (
    parse_github_url,
    fetch_repo_basic,
    fetch_repo_tree,
    save_repo_data
)

router = APIRouter()


@router.post("/info", response_model=RepoInfoResponse)
async def get_repo_info(body: RepoInfoRequest):
    """
    Given a GitHub URL, return basic repo info + a list of file paths.
    """
    owner, repo = parse_github_url(str(body.github_url))
    basic = await fetch_repo_basic(owner, repo)
    tree = await fetch_repo_tree(owner, repo, max_items=100)

    data = {**basic, "file_paths": tree}
    save_repo_data(owner, repo, data)  # optional caching

    return RepoInfoResponse(**data)
