FINDINGS_EXTRACTION_PROMPT = """\
You are extracting structured fraud/workflow risk findings from an assessment text.

Return ONLY valid JSON matching this schema:
{
  "company_name": string|null,
  "findings": [
    {
      "title": string,
      "category": string,
      "severity": "low"|"medium"|"high"|"critical",
      "systems_touched": [string],
      "evidence": [{"snippet": string, "source": "assessment_text"}],
      "recommended_actions": [string],
      "confidence": number
    }
  ]
}

Rules:
- Every finding MUST include at least 1 evidence snippet copied from the text.
- Keep evidence snippets short (1–2 sentences).
- If unsure, lower confidence.
"""

CISO_BRIEF_PROMPT = """\
You are writing a CISO-facing brief from structured findings.

Output markdown with sections:
- Executive summary (3-5 bullets)
- Top risks (ranked)
- Control gaps (what current controls likely miss)
- Recommended next steps (30 days)

Be concrete and reference the finding titles.
"""

CTO_BRIEF_PROMPT = """\
You are writing a CTO-facing brief from structured findings.

Output markdown with sections:
- Executive summary (3-5 bullets)
- Systems & integrations impacted
- Trust boundaries & workflow weaknesses
- Recommended next steps (30 days)

Be concrete and reference the finding titles and systems_touched.
"""
