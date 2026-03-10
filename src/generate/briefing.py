from openai import OpenAI
from src.core.config import settings
from src.generate.prompts import CISO_BRIEF_PROMPT, CTO_BRIEF_PROMPT
from src.core.schemas import FindingsBundle

def _make_client() -> OpenAI:
    if not settings.openai_api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in .env")
    return OpenAI(api_key=settings.openai_api_key)

def generate_ciso_brief(bundle: FindingsBundle) -> str:
    client = _make_client()
    resp = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": CISO_BRIEF_PROMPT},
            {"role": "user", "content": bundle.model_dump_json()},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()

def generate_cto_brief(bundle: FindingsBundle) -> str:
    client = _make_client()
    resp = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": CTO_BRIEF_PROMPT},
            {"role": "user", "content": bundle.model_dump_json()},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()