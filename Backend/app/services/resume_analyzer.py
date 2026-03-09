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

IMPORTANT_PHRASES = {
    "machine learning": 3,
    "data analysis": 3,
    "data science": 3,
    "project management": 3,
    "software engineering": 3,
    "web development": 2,
    "frontend development": 2,
    "backend development": 2,
    "full stack": 2,
    "rest api": 3,
    "cloud deployment": 2,
    "version control": 2,
    "problem solving": 2,
    "team leadership": 2,
    "user experience": 2,
    "database management": 2,
    "artificial intelligence": 3
}

IMPORTANT_SINGLE_KEYWORDS = {
    "python": 3,
    "fastapi": 3,
    "react": 3,
    "javascript": 3,
    "typescript": 3,
    "sql": 3,
    "docker": 3,
    "aws": 3,
    "api": 2,
    "git": 2,
    "mongodb": 2,
    "postgresql": 2,
    "node.js": 2,
    "java": 2,
    "communication": 2,
    "leadership": 2,
    "teamwork": 2,
    "analytics": 2
}

SECTION_PATTERNS = {
    "summary": [
        "summary", "professional summary", "profile", "about me"
    ],
    "skills": [
        "skills", "technical skills", "core skills", "competencies"
    ],
    "experience": [
        "experience", "work experience", "employment history", "professional experience"
    ],
    "projects": [
        "projects", "personal projects", "academic projects"
    ],
    "education": [
        "education", "academic background", "qualifications"
    ]
}


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def clean_and_tokenize(text: str) -> set:
    text = normalize_text(text)
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


def split_resume_into_sections(resume_text: str) -> dict:
    lines = [line.strip() for line in resume_text.splitlines() if line.strip()]
    sections = {
        "summary": "",
        "skills": "",
        "experience": "",
        "projects": "",
        "education": "",
        "other": ""
    }

    current_section = "other"

    for line in lines:
        lower_line = line.lower()

        matched_section = None
        for section_name, headings in SECTION_PATTERNS.items():
            if lower_line in headings:
                matched_section = section_name
                break

        if matched_section:
            current_section = matched_section
        else:
            sections[current_section] += line + " "

    return {key: value.strip() for key, value in sections.items()}


def extract_matched_phrases(resume_text: str, job_text: str) -> list:
    matched_phrases = []
    for phrase in IMPORTANT_PHRASES:
        if phrase in job_text and phrase in resume_text:
            matched_phrases.append(phrase)
    return sorted(matched_phrases)


def extract_missing_phrases(resume_text: str, job_text: str) -> list:
    missing_phrases = []
    for phrase in IMPORTANT_PHRASES:
        if phrase in job_text and phrase not in resume_text:
            missing_phrases.append(phrase)
    return sorted(missing_phrases)


def extract_relevant_job_keywords(job_keywords: set) -> list:
    relevant_keywords = []
    for word in job_keywords:
        if word in IMPORTANT_SINGLE_KEYWORDS:
            relevant_keywords.append(word)
    return sorted(relevant_keywords)


def calculate_weighted_score(
    matched_keywords: list,
    job_keywords: list,
    matched_phrases: list,
    missing_phrases: list
) -> int:
    total_possible = 0
    total_matched = 0

    for keyword in job_keywords:
        weight = IMPORTANT_SINGLE_KEYWORDS.get(keyword, 1)
        total_possible += weight
        if keyword in matched_keywords:
            total_matched += weight

    phrase_pool = set(matched_phrases + missing_phrases)
    for phrase in phrase_pool:
        weight = IMPORTANT_PHRASES.get(phrase, 1)
        total_possible += weight
        if phrase in matched_phrases:
            total_matched += weight

    if total_possible == 0:
        return 0

    return round((total_matched / total_possible) * 100)


def find_keywords_by_section(sections: dict, keywords: list, phrases: list) -> dict:
    section_map = {}

    for section_name, content in sections.items():
        normalized_content = normalize_text(content)
        tokens_in_section = clean_and_tokenize(content)

        found_items = []

        for keyword in keywords:
            if keyword in tokens_in_section:
                found_items.append(keyword)

        for phrase in phrases:
            if phrase in normalized_content:
                found_items.append(phrase)

        section_map[section_name] = sorted(set(found_items))

    return section_map


def generate_section_based_suggestions(
    sections: dict,
    missing_keywords: list,
    missing_phrases: list,
    section_matches: dict,
    match_score: int
) -> list:
    suggestions = []

    summary_content = sections.get("summary", "")
    skills_matches = section_matches.get("skills", [])
    experience_matches = section_matches.get("experience", [])
    project_matches = section_matches.get("projects", [])

    if not summary_content:
        suggestions.append(
            "Add a professional summary tailored to the target role so recruiters can quickly see your fit."
        )
    elif len(summary_content.split()) < 20:
        suggestions.append(
            "Your summary is too brief. Expand it to reflect your target role, strongest skills, and value clearly."
        )

    if missing_keywords or missing_phrases:
        suggestions.append(
            "Add missing job-relevant keywords naturally into the most relevant sections of your resume, especially skills, experience, and projects."
        )

    if skills_matches and not experience_matches:
        suggestions.append(
            "You list relevant skills, but they are not well supported in your experience section. Show where you actually used those tools or skills."
        )

    if project_matches and not experience_matches:
        suggestions.append(
            "Your projects help support your fit, but your experience section is still weak for this role. Strengthen work experience bullets with relevant achievements."
        )

    if not skills_matches:
        suggestions.append(
            "Your skills section does not clearly reflect the target job requirements. Add relevant tools, technologies, and competencies that you genuinely have."
        )

    if match_score < 40:
        suggestions.append(
            "Your resume is weakly aligned with the job. Rewrite key sections to better match the language, tools, and responsibilities in the job description."
        )
    elif match_score < 70:
        suggestions.append(
            "Your resume has moderate alignment. Improve it by making your experience bullets more role-specific and more results-driven."
        )
    else:
        suggestions.append(
            "Your resume is strongly aligned. Focus on sharpening wording, outcomes, and impact."
        )

    if missing_phrases:
        suggestions.append(
            f"Try to reflect these missing concepts if they genuinely match your background: {', '.join(missing_phrases)}."
        )

    if missing_keywords:
        suggestions.append(
            f"Consider highlighting these missing keywords where relevant: {', '.join(missing_keywords)}."
        )

    return suggestions


def analyze_resume(resume_text: str, job_description: str) -> dict:
    normalized_resume = normalize_text(resume_text)
    normalized_job = normalize_text(job_description)

    sections = split_resume_into_sections(resume_text)

    resume_keywords = clean_and_tokenize(resume_text)
    job_keywords_raw = clean_and_tokenize(job_description)

    relevant_job_keywords = extract_relevant_job_keywords(job_keywords_raw)

    matched_keywords = sorted(resume_keywords.intersection(set(relevant_job_keywords)))
    missing_keywords = sorted(set(relevant_job_keywords).difference(resume_keywords))

    matched_phrases = extract_matched_phrases(normalized_resume, normalized_job)
    missing_phrases = extract_missing_phrases(normalized_resume, normalized_job)

    match_score = calculate_weighted_score(
        matched_keywords=matched_keywords,
        job_keywords=relevant_job_keywords,
        matched_phrases=matched_phrases,
        missing_phrases=missing_phrases
    )

    section_matches = find_keywords_by_section(
        sections=sections,
        keywords=matched_keywords,
        phrases=matched_phrases
    )

    improvement_suggestions = generate_section_based_suggestions(
        sections=sections,
        missing_keywords=missing_keywords,
        missing_phrases=missing_phrases,
        section_matches=section_matches,
        match_score=match_score
    )

    combined_matched = sorted(set(matched_keywords + matched_phrases))
    combined_missing = sorted(set(missing_keywords + missing_phrases))

    return {
        "match_score": match_score,
        "matched_keywords": combined_matched,
        "missing_keywords": combined_missing,
        "improvement_suggestions": improvement_suggestions
    }