import json
from openai import OpenAI
from src.core.config import settings
from src.generate.prompts import FINDINGS_EXTRACTION_PROMPT
from src.core.schemas import FindingsBundle

def extract_findings(assessment_text: str) -> FindingsBundle:
    if not settings.openai_api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in .env")

    client = OpenAI(api_key=settings.openai_api_key)

    resp = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": FINDINGS_EXTRACTION_PROMPT},
            {"role": "user", "content": assessment_text},
        ],
        temperature=0.2,
    )

    raw = resp.choices[0].message.content
    if raw is None:
        raise RuntimeError("Model returned no content.")

    raw = raw.strip()

    print("\n===== RAW MODEL OUTPUT =====\n")
    print(raw)
    print("\n============================\n")

    # Remove markdown code fences if present
    if raw.startswith("```json"):
        raw = raw[len("```json"):].strip()
        if raw.endswith("```"):
            raw = raw[:-3].strip()
    elif raw.startswith("```"):
        raw = raw[3:].strip()
        if raw.endswith("```"):
            raw = raw[:-3].strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Model did not return valid JSON.\nRaw output was:\n{raw}") from e

    return FindingsBundle.model_validate(data)