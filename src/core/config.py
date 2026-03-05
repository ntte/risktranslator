from dataclasses import dataclass
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

@dataclass(frozen=True)
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    model: str = os.getenv("MODEL", "gpt-4.1-mini")
    project_root: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = project_root / "data"

settings = Settings()
