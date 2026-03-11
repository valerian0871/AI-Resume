from pydantic import BaseModel
from typing import List, Dict, Union


class AnalysisResponse(BaseModel):
    match_score: int
    matched_keywords: List[str]
    missing_keywords: List[str]
    improvement_suggestions: List[str]
    tailored_resume_suggestions: Dict[str, Union[List[str], str]]