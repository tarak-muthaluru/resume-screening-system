import re
from typing import Dict, List


def _find_first(text_lower: str, keywords: List[str]) -> int:
    """
    Find the first index of any keyword in the lowercase text.
    Returns -1 if not found.
    """
    positions = []
    for kw in keywords:
        pos = text_lower.find(kw.lower())
        if pos != -1:
            positions.append(pos)

    if not positions:
        return -1
    return min(positions)


def extract_between_sections(text: str,
                             start_keywords: List[str],
                             end_keywords: List[str]) -> str:
    """
    Extract text between a 'start' heading and the next 'end' heading.
    If no end heading is found, returns text till the end.
    If start is not found, returns empty string.
    """
    text_lower = text.lower()

    start_idx = _find_first(text_lower, start_keywords)
    if start_idx == -1:
        return ""

    # Move start index to just after the start keyword that matched
    # (we will find the exact keyword used at that position)
    used_kw = None
    for kw in start_keywords:
        if text_lower.startswith(kw.lower(), start_idx):
            used_kw = kw
            break

    if used_kw is None:
        # Fallback: just use the first keyword length
        used_kw = start_keywords[0]

    content_start = start_idx + len(used_kw)

    # Find the next end keyword after content_start
    end_search_region = text_lower[content_start:]
    end_rel_idx = _find_first(end_search_region, end_keywords)

    if end_rel_idx == -1:
        # No end heading found -> go till end
        content_end = len(text)
    else:
        content_end = content_start + end_rel_idx

    section_text = text[content_start:content_end].strip()
    return section_text


def extract_resume_sections(text: str) -> Dict[str, str]:
    """
    Extract main sections from a resume text using simple keyword heuristics.
    Currently focuses on 'skills' and 'experience'.

    Returns a dict with keys: 'skills', 'experience'.
    Some values may be empty strings if not found.
    """
    # We keep the original text, but normalize spacing a bit
    text = re.sub(r"\s+", " ", text)

    # Define possible headings
    skills_starts = [
        "skills",
        "technical skills",
        "core skills",
        "key skills"
    ]

    experience_starts = [
        "experience",
        "work experience",
        "professional experience",
        "employment history"
    ]

    # Possible "next sections" after skills or experience
    after_skills = experience_starts + [
        "projects",
        "education",
        "certifications",
        "summary",
        "profile"
    ]

    after_experience = [
        "education",
        "projects",
        "certifications",
        "skills",
        "summary",
        "profile"
    ]

    skills_text = extract_between_sections(text, skills_starts, after_skills)
    experience_text = extract_between_sections(text, experience_starts, after_experience)

    return {
        "skills": skills_text,
        "experience": experience_text,
    }
