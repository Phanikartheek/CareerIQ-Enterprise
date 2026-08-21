"""
=========================================================
Resume Intelligence AI
Feature Engineering Module
Author : Vellanki phanikartheek
Version : 5.0
=========================================================
"""

import re

class FeatureEngineering:

    def __init__(self):
        pass

    # -----------------------------------
    # Experience Extraction
    # -----------------------------------

    def extract_experience(self, text):

        text = text.lower()

        patterns = [

            r'(\d+)\+?\s*years',

            r'(\d+)\s*yrs',

            r'(\d+)\s*year',

            r'experience\s*[:\-]?\s*(\d+)'

        ]

        for pattern in patterns:

            match = re.search(pattern, text)

            if match:

                return int(match.group(1))

        return 0

    # -----------------------------------
    # Email
    # -----------------------------------

    def has_email(self, text):

        pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

        return 1 if re.search(pattern, text) else 0

    # -----------------------------------
    # Phone
    # -----------------------------------

    def has_phone(self, text):

        pattern = r'(\+91)?[6-9]\d{9}'

        return 1 if re.search(pattern, text) else 0

    # -----------------------------------
    # LinkedIn
    # -----------------------------------

    def has_linkedin(self, text):

        return 1 if "linkedin.com" in text.lower() else 0

    # -----------------------------------
    # GitHub
    # -----------------------------------

    def has_github(self, text):

        return 1 if "github.com" in text.lower() else 0

    # -----------------------------------
    # Projects
    # -----------------------------------

    def project_count(self, text):

        keywords = [

            "project",

            "projects",

            "developed",

            "implemented",

            "designed",

            "built"

        ]

        count = 0

        lower = text.lower()

        for word in keywords:

            count += lower.count(word)

        return count

    # -----------------------------------
    # Certifications
    # -----------------------------------

    def certification_count(self, text):

        keywords = [

            "certificate",

            "certification",

            "certified",

            "coursera",

            "udemy",

            "linkedin learning",

            "google",

            "microsoft",

            "aws"

        ]

        count = 0

        lower = text.lower()

        for word in keywords:

            count += lower.count(word)

        return count

    # -----------------------------------
    # Education
    # -----------------------------------

    def education_level(self, text):

        text = text.lower()

        if "phd" in text:

            return "PhD"

        elif "m.tech" in text or "master" in text:

            return "Masters"

        elif "b.tech" in text or "bachelor" in text:

            return "Bachelors"

        elif "diploma" in text:

            return "Diploma"

        return "Unknown"

    # -----------------------------------
    # Resume Length
    # -----------------------------------

    def word_count(self, text):

        return len(text.split())

    # -----------------------------------
    # Resume Score
    # -----------------------------------

    def quality_score(self, text):

        score = 0

        wc = self.word_count(text)

        if wc > 400:
            score += 20

        if self.has_email(text):
            score += 10

        if self.has_phone(text):
            score += 10

        if self.has_linkedin(text):
            score += 10

        if self.has_github(text):
            score += 10

        score += min(self.project_count(text) * 5,20)

        score += min(self.certification_count(text) * 5,20)

        score += min(self.extract_experience(text) * 2,20)

        return min(score,100)

    # -----------------------------------
    # Feature Vector
    # -----------------------------------

    def generate_features(self,text):

        features = {

            "Experience": self.extract_experience(text),

            "Education": self.education_level(text),

            "Resume Words": self.word_count(text),

            "Projects": self.project_count(text),

            "Certifications": self.certification_count(text),

            "Email": self.has_email(text),

            "Phone": self.has_phone(text),

            "LinkedIn": self.has_linkedin(text),

            "GitHub": self.has_github(text),

            "Resume Quality Score": self.quality_score(text)

        }

        return features