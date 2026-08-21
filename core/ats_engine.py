"""
=========================================================
CareerIQ Enterprise
Enterprise ATS Engine
Version : 10.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import re


class ATSEngine:

    def __init__(self):

        self.required_sections = [

            "education",
            "experience",
            "skills",
            "projects",
            "certifications"

        ]

    # =====================================================
    # Extract Skills
    # =====================================================

    def extract_skills(

        self,

        resume_text,

        skill_database

    ):

        resume_lower = resume_text.lower()

        matched = []

        missing = []

        for skill in skill_database:

            if skill.lower() in resume_lower:

                matched.append(skill)

            else:

                missing.append(skill)

        return matched, missing

    # =====================================================
    # Contact Validation
    # =====================================================

    def contact_score(

        self,

        parsed_resume

    ):

        score = 0

        if parsed_resume.get("email"):
            score += 25

        if parsed_resume.get("phone"):
            score += 25

        if parsed_resume.get("linkedin"):
            score += 25

        if parsed_resume.get("github"):
            score += 25

        return score

    # =====================================================
    # Resume Length
    # =====================================================

    def length_score(

        self,

        word_count

    ):

        if 500 <= word_count <= 900:
            return 100

        elif 350 <= word_count <= 1200:
            return 80

        elif 250 <= word_count <= 1500:
            return 60

        else:
            return 40

    # =====================================================
    # Section Score
    # =====================================================

    def section_score(

        self,

        resume_text

    ):

        resume = resume_text.lower()

        found = []

        missing = []

        for section in self.required_sections:

            if section in resume:

                found.append(section.title())

            else:

                missing.append(section.title())

        score = int(

            (len(found) / len(self.required_sections)) * 100

        )

        return score, found, missing

    # =====================================================
    # Formatting Score
    # =====================================================

    def formatting_score(

        self,

        resume_text

    ):

        score = 100

        if len(resume_text.splitlines()) < 10:
            score -= 20

        if len(resume_text) < 1500:
            score -= 20

        if resume_text.count("•") == 0 and resume_text.count("-") == 0:
            score -= 10

        return max(score, 40)

    # =====================================================
    # Keyword Score
    # =====================================================

    def keyword_score(

        self,

        matched,

        missing

    ):

        total = len(matched) + len(missing)

        if total == 0:
            return 0

        return round(

            len(matched) / total * 100,

            2

        )

    # =====================================================
    # Grade
    # =====================================================

    def grade(

        self,

        score

    ):

        if score >= 95:
            return "A+"

        elif score >= 90:
            return "A"

        elif score >= 80:
            return "B+"

        elif score >= 70:
            return "B"

        elif score >= 60:
            return "C"

        return "D"

    # =====================================================
    # Recommendation
    # =====================================================

    def recommendation(

        self,

        score

    ):

        if score >= 90:
            return "Highly Recommended"

        elif score >= 80:
            return "Recommended"

        elif score >= 70:
            return "Good Resume"

        elif score >= 60:
            return "Needs Improvement"

        return "Poor ATS Resume"

    # =====================================================
    # Complete ATS Report
    # =====================================================

    def analyze(

        self,

        parsed_resume,

        skill_database

    ):

        resume_text = parsed_resume.get(

            "raw_text",

            ""

        )

        words = parsed_resume.get(

            "word_count",

            0

        )

        matched, missing = self.extract_skills(

            resume_text,

            skill_database

        )

        keyword = self.keyword_score(

            matched,

            missing

        )

        section, found_sections, missing_sections = self.section_score(

            resume_text

        )

        contact = self.contact_score(

            parsed_resume

        )

        formatting = self.formatting_score(

            resume_text

        )

        length = self.length_score(

            words

        )

        ats_score = round(

            keyword * 0.40 +

            section * 0.20 +

            contact * 0.10 +

            formatting * 0.15 +

            length * 0.15,

            2

        )

        ats_score = min(100, ats_score)

        return {

            "ATS Score": ats_score,

            "Grade": self.grade(ats_score),

            "Recommendation": self.recommendation(ats_score),

            "Keyword Score": keyword,

            "Section Score": section,

            "Formatting Score": formatting,

            "Contact Score": contact,

            "Length Score": length,

            "Matched Skills": matched,

            "Missing Skills": missing,

            "Found Sections": found_sections,

            "Missing Sections": missing_sections

        }
