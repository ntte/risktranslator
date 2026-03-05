from pydantic import BaseModel, Field
from typing import List, Literal, Optional

Severity = Literal["low", "medium", "high", "critical"]

class Evidence(BaseModel):
    snippet: str
    source: str = "assessment_text"

class Finding(BaseModel):
    title: str
    category: str
    severity: Severity
    systems_touched: List[str] = Field(default_factory=list)
    evidence: List[Evidence] = Field(default_factory=list)
    recommended_actions: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.7)

class FindingsBundle(BaseModel):
    company_name: Optional[str] = None
    findings: List[Finding]
