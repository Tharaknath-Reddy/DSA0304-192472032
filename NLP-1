"""
Q1. Resume Information Extraction using Regular Expressions

This program extracts candidate details from resume text and displays
only candidates who satisfy the eligibility criteria:
minimum 2 years of experience and Python skill.
"""

import re
from dataclasses import dataclass


TECHNICAL_SKILLS = ["Python", "Java", "SQL", "Machine Learning", "NLP"]


@dataclass
class CandidateProfile:
    name: str
    emails: list[str]
    mobile_numbers: list[str]
    skills: list[str]
    years_experience: float
    eligible: bool


def extract_candidate_name(resume_text: str) -> str:
    name_pattern = re.compile(r"(?im)^\s*(?:Name|Candidate Name)\s*:\s*([A-Z][A-Za-z .'-]+)$")
    match = name_pattern.search(resume_text)
    if match:
        return match.group(1).strip()

    first_line = resume_text.strip().splitlines()[0].strip()
    if re.fullmatch(r"[A-Z][A-Za-z .'-]{2,}", first_line):
        return first_line
    return "Name not found"


def extract_emails(resume_text: str) -> list[str]:
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    return sorted(set(email_pattern.findall(resume_text)))


def extract_mobile_numbers(resume_text: str) -> list[str]:
    mobile_pattern = re.compile(r"(?:\+91[-\s]?)?[6-9]\d{9}\b")
    return sorted(set(mobile_pattern.findall(resume_text)))


def extract_technical_skills(resume_text: str) -> list[str]:
    detected_skills = []
    for skill in TECHNICAL_SKILLS:
        skill_pattern = re.compile(rf"\b{re.escape(skill)}\b", re.IGNORECASE)
        if skill_pattern.search(resume_text):
            detected_skills.append(skill)
    return detected_skills


def extract_years_experience(resume_text: str) -> float:
    experience_pattern = re.compile(
        r"(\d+(?:\.\d+)?)\s*(?:\+?\s*)?(?:years?|yrs?)\s+(?:of\s+)?experience",
        re.IGNORECASE,
    )
    match = experience_pattern.search(resume_text)
    return float(match.group(1)) if match else 0.0


def build_candidate_profile(resume_text: str) -> CandidateProfile:
    skills = extract_technical_skills(resume_text)
    years_experience = extract_years_experience(resume_text)
    eligible = years_experience >= 2 and "Python" in skills

    return CandidateProfile(
        name=extract_candidate_name(resume_text),
        emails=extract_emails(resume_text),
        mobile_numbers=extract_mobile_numbers(resume_text),
        skills=skills,
        years_experience=years_experience,
        eligible=eligible,
    )


def display_profile(profile: CandidateProfile) -> None:
    print("-" * 60)
    print(f"Candidate Name      : {profile.name}")
    print(f"Email Address(es)   : {', '.join(profile.emails) if profile.emails else 'Not found'}")
    print(f"Mobile Number(s)    : {', '.join(profile.mobile_numbers) if profile.mobile_numbers else 'Not found'}")
    print(f"Technical Skills    : {', '.join(profile.skills) if profile.skills else 'Not found'}")
    print(f"Years of Experience : {profile.years_experience}")
    print(f"Eligibility Status  : {'Eligible' if profile.eligible else 'Not Eligible'}")


def main() -> None:
    resumes = [
        """Name: Ananya Sharma
Email: ananya.sharma@example.com
Mobile: +91 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years of experience in NLP projects.""",
        """Candidate Name: Rahul Menon
Email: rahul.menon@example.com
Mobile: 8123456789
Skills: Java, SQL
Experience: 1 year of experience in backend development.""",
        """Name: Priya Nair
Email: priya.nair@example.com
Mobile: 9988776655
Skills: Python, Java, SQL
Experience: 2.5 years of experience in software development.""",
    ]

    profiles = [build_candidate_profile(resume) for resume in resumes]

    print("STRUCTURED CANDIDATE PROFILE SUMMARY")
    for profile in profiles:
        display_profile(profile)

    print("\nSHORTLISTED CANDIDATES")
    eligible_profiles = [profile for profile in profiles if profile.eligible]
    if not eligible_profiles:
        print("No candidates satisfy the eligibility criteria.")
    else:
        for profile in eligible_profiles:
            print(f"{profile.name} is shortlisted.")


if __name__ == "__main__":
    main()
