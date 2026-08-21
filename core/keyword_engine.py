"""
=========================================================
CareerIQ Enterprise
Enterprise Keyword Engine
Version : 11.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import re

from core.skill_database import MASTER_SKILLS
from core.alias_database import ALIASES
from core.skill_categories import SKILL_CATEGORIES
from core.role_database import ROLE_SKILLS


class KeywordEngine:

    def __init__(self):

        self.master_skills = sorted(
            MASTER_SKILLS,
            key=len,
            reverse=True
        )

        self.skills = self.master_skills

    # =====================================================
    # Normalize Text
    # =====================================================

    def normalize(self, text):

        return text.lower()

    # =====================================================
    # Apply Skill Aliases
    # =====================================================

    def apply_aliases(self, text):

        text = text.lower()

        for alias, actual in ALIASES.items():

            pattern = r"\b" + re.escape(alias.lower()) + r"\b"

            text = re.sub(
                pattern,
                actual.lower(),
                text
            )

        return text

    # =====================================================
    # Extract Skills
    # =====================================================

    def extract_skills(self, text):

        text = self.apply_aliases(text)

        found = []

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):

                found.append(skill)

        return sorted(list(set(found)))

    # =====================================================
    # Skill Categories
    # =====================================================

    def categorize(self, skills):

        result = {}

        for category, values in SKILL_CATEGORIES.items():

            matched = []

            for skill in values:

                if skill in skills:

                    matched.append(skill)

            if matched:

                result[category] = matched

        return result

    # =====================================================
    # Skill Frequency
    # =====================================================

    def frequency(self, text):

        text = self.apply_aliases(text)

        freq = {}

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            count = len(
                re.findall(
                    pattern,
                    text
                )
            )

            if count > 0:

                freq[skill] = count

        return dict(

            sorted(

                freq.items(),

                key=lambda x: x[1],

                reverse=True

            )

        )

    # =====================================================
    # Match Against Job Role
    # =====================================================

    def role_match(

        self,

        detected_skills,

        role

    ):

        required = ROLE_SKILLS.get(

            role,

            []

        )

        matched = []

        missing = []

        for skill in required:

            if skill in detected_skills:

                matched.append(skill)

            else:

                missing.append(skill)

        coverage = 0

        if required:

            coverage = round(

                len(matched)

                /

                len(required)

                * 100,

                2

            )

        return {

            "Role": role,

            "Coverage": coverage,

            "Matched Skills": matched,

            "Missing Skills": missing

        }

    # =====================================================
    # Enterprise Analysis
    # =====================================================

    def analyze(

        self,

        text,

        role=None

    ):

        skills = self.extract_skills(text)

        report = {

            "Skills": skills,

            "Skill Count": len(skills),

            "Categories": self.categorize(skills),

            "Frequency": self.frequency(text)

        }

        if role:

            report["Role Analysis"] = self.role_match(

                skills,

                role

            )

        return report