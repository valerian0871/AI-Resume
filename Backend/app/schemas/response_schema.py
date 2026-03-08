# backend/app/schemas/response_schema.py

from pydantic import BaseModel
from typing import List

class AnalysisResponse(BaseModel):
    match_score: int
    matched_keywords: List[str]
    missing_keywords: List[str]
    improvement_suggestions: List[str]