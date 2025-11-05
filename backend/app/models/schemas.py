from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class RepoInfoRequest(BaseModel):
    github_url: HttpUrl


class RepoInfoResponse(BaseModel):
    name: str
    full_name: str
    description: Optional[str] = None
    html_url: HttpUrl
    default_branch: str
    language: Optional[str] = None
    topics: List[str] = []
    stargazers_count: int
    forks_count: int
    open_issues_count: int
    file_paths: List[str] = []
