
from pathlib import Path

def load_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p}")
    return p.read_text(encoding="utf-8", errors="ignore")
