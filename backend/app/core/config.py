import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")
        self.allowed_origins: List[str] = [o.strip() for o in origins.split(",")]

settings = Settings()
