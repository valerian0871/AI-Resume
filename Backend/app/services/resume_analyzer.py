# backend/app/services/resume_analyzer.py

import re

def clean_and_tokenize(text: str):
    text = text.lower()
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    return set(words)

def analyze_resume(resume_text: str, job_description: str):
    resume_words = clean_and_tokenize(resume_text)
    job_words = clean_and_tokenize(job_description)

    matched_keywords = sorted(list(resume_words.intersection(job_words)))
    missing_keywords = sorted(list(job_words.difference(resume_words)))

    if len(job_words) == 0:
        match_score = 0
    else:
        match_score = int((len(matched_keywords) / len(job_words)) * 100)

    suggestions = []

    if missing_keywords:
        suggestions.append("Add more job-specific keywords from the description into your resume where relevant.")
    if match_score < 50:
        suggestions.append("Your resume is not well aligned with this role yet. Tailor your summary, skills, and experience sections.")
    if 50 <= match_score < 75:
        suggestions.append("Your resume has partial alignment. Improve it by adding stronger role-specific achievements and terminology.")
    if match_score >= 75:
        suggestions.append("Your resume is strongly aligned. Focus on polishing wording and highlighting measurable achievements.")

    if "python" in missing_keywords:
        suggestions.append("Consider mentioning Python experience if you have used it in projects or work.")
    if "react" in missing_keywords:
        suggestions.append("Consider adding React-related experience if it matches your background.")

    return {
        "match_score": match_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "improvement_suggestions": suggestions
    }