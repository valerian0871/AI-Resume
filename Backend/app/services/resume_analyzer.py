import re

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by",
    "for", "from", "if", "in", "into", "is", "it", "no",
    "not", "of", "on", "or", "such", "that", "the", "their",
    "then", "there", "these", "they", "this", "to", "was",
    "will", "with", "we", "you", "your", "our", "should",
    "can", "have", "has", "had", "were", "been", "being",
    "do", "does", "did", "so", "than", "too", "very"
}

def clean_and_tokenize(text: str) -> set:
    text = text.lower()

    # Extract words, numbers, and simple tech terms
    tokens = re.findall(r"\b[a-zA-Z][a-zA-Z0-9+#.-]*\b", text)

    cleaned_tokens = set()

    for token in tokens:
        token = token.strip(".-,")
        if token in STOPWORDS:
            continue
        if len(token) < 3:
            continue
        cleaned_tokens.add(token)

    return cleaned_tokens

def calculate_match_score(matched_keywords: list, job_keywords: list) -> int:
    if not job_keywords:
        return 0
    return round((len(matched_keywords) / len(job_keywords)) * 100)

def generate_suggestions(match_score: int, missing_keywords: list) -> list:
    suggestions = []

    if missing_keywords:
        suggestions.append(
            "Add relevant missing keywords from the job description into your resume, especially in your skills, summary, and work experience sections."
        )

    if match_score < 40:
        suggestions.append(
            "Your resume is weakly aligned with this job. Tailor it more directly to the role by matching the required tools, skills, and responsibilities."
        )
    elif match_score < 70:
        suggestions.append(
            "Your resume shows partial alignment. Strengthen it by emphasizing relevant projects, measurable achievements, and job-specific terminology."
        )
    else:
        suggestions.append(
            "Your resume is strongly aligned with this role. Focus on polishing your bullet points and making your achievements more measurable."
        )

    technical_keywords = {"python", "fastapi", "react", "sql", "docker", "aws", "api", "javascript"}
    soft_keywords = {"communication", "leadership", "teamwork", "collaboration", "problem-solving"}

    missing_technical = [word for word in missing_keywords if word in technical_keywords]
    missing_soft = [word for word in missing_keywords if word in soft_keywords]

    if missing_technical:
        suggestions.append(
            f"Consider adding evidence of these technical skills if you truly have them: {', '.join(missing_technical)}."
        )

    if missing_soft:
        suggestions.append(
            f"Highlight these soft skills where appropriate: {', '.join(missing_soft)}."
        )

    return suggestions

def analyze_resume(resume_text: str, job_description: str) -> dict:
    resume_keywords = clean_and_tokenize(resume_text)
    job_keywords = clean_and_tokenize(job_description)

    matched_keywords = sorted(resume_keywords.intersection(job_keywords))
    missing_keywords = sorted(job_keywords.difference(resume_keywords))

    match_score = calculate_match_score(matched_keywords, list(job_keywords))
    improvement_suggestions = generate_suggestions(match_score, missing_keywords)

    return {
        "match_score": match_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "improvement_suggestions": improvement_suggestions
    }