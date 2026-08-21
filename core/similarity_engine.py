"""
=========================================================
CareerIQ Enterprise
Enterprise NLP Similarity Engine
Version : 11.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from core.keyword_engine import KeywordEngine


class SimilarityEngine:

    def __init__(self):

        self.keyword_engine = KeywordEngine()

        self.vectorizer = TfidfVectorizer(

            stop_words="english",

            lowercase=True,

            ngram_range=(1, 2)

        )

    # =====================================================
    # CLEAN TEXT
    # =====================================================

    def clean_text(self, text):

        if text is None:

            return ""

        text = str(text)

        text = text.lower()

        text = re.sub(

            r"[^a-zA-Z0-9+#.]",

            " ",

            text

        )

        text = re.sub(

            r"\s+",

            " ",

            text

        )

        return text.strip()

    # =====================================================
    # TF-IDF
    # =====================================================

    def vectorize(

        self,

        resume,

        job

    ):

        resume = self.clean_text(resume)

        job = self.clean_text(job)

        vectors = self.vectorizer.fit_transform(

            [

                resume,

                job

            ]

        )

        return vectors

    # =====================================================
    # COSINE SIMILARITY
    # =====================================================

    def similarity_score(

        self,

        resume,

        job

    ):

        if not resume:

            return 0

        if not job:

            return 0

        vectors = self.vectorize(

            resume,

            job

        )

        score = cosine_similarity(

            vectors[0],

            vectors[1]

        )[0][0]

        return round(

            score * 100,

            2

        )

    # =====================================================
    # KEYWORD MATCH
    # =====================================================

    def keyword_match(

        self,

        resume,

        job

    ):

        resume_words = set(

            self.clean_text(

                resume

            ).split()

        )

        job_words = set(

            self.clean_text(

                job

            ).split()

        )

        if len(job_words) == 0:

            return 0

        matched = resume_words.intersection(

            job_words

        )

        return round(

            len(matched)

            /

            len(job_words)

            *

            100,

            2

        )
    # =====================================================
    # SKILL MATCH
    # =====================================================

    def skill_match(

        self,

        resume,

        job

    ):

        resume_skills = self.keyword_engine.extract_skills(

            resume

        )

        job_skills = self.keyword_engine.extract_skills(

            job

        )

        matched = []

        missing = []

        for skill in job_skills:

            if skill in resume_skills:

                matched.append(skill)

            else:

                missing.append(skill)

        coverage = 0

        if len(job_skills) > 0:

            coverage = round(

                len(matched)

                /

                len(job_skills)

                * 100,

                2

            )

        return {

            "Resume Skills": resume_skills,

            "Job Skills": job_skills,

            "Matched Skills": matched,

            "Missing Skills": missing,

            "Skill Coverage": coverage

        }

    # =====================================================
    # OVERALL MATCH
    # =====================================================

    def overall_match(

        self,

        similarity,

        keyword,

        skill

    ):
        # Skill Coverage : 50% weight  (most important — actual skill alignment)
        # Keyword Match  : 30% weight  (keyword overlap with JD)
        # TF-IDF Sim     : 20% weight  (cosine similarity — naturally lower, less weight)
        score = (

            similarity * 0.20 +

            keyword * 0.30 +

            skill * 0.50

        )

        return round(score, 2)

    # =====================================================
    # GRADE
    # =====================================================

    def grade(

        self,

        score

    ):

        if score >= 95:

            return "A+"

        elif score >= 85:

            return "A"

        elif score >= 75:

            return "B+"

        elif score >= 65:

            return "B"

        elif score >= 50:

            return "C"

        return "D"

    # =====================================================
    # CONFIDENCE
    # =====================================================

    def confidence(

        self,

        score

    ):

        if score >= 90:

            return "Very High"

        elif score >= 80:

            return "High"

        elif score >= 65:

            return "Medium"

        return "Low"

    # =====================================================
    # ATS SCORE
    # =====================================================

    def ats_score(

        self,

        overall

    ):

        ats = overall * 1.05

        if ats > 100:

            ats = 100

        return round(ats, 2)
    # =====================================================
    # HIRING STATUS
    # =====================================================

    def hiring_status(self, score):

        if score >= 95:
            return "🟢 Outstanding Match"

        elif score >= 85:
            return "🟢 Highly Recommended"

        elif score >= 75:
            return "🟡 Recommended"

        elif score >= 60:
            return "🟠 Consider After Review"

        return "🔴 Poor Match"

    # =====================================================
    # RECRUITER DECISION
    # =====================================================

    def recruiter_decision(self, score):

        if score >= 90:
            return "Proceed to Technical Interview"

        elif score >= 75:
            return "Shortlist Candidate"

        elif score >= 60:
            return "Keep for Future Review"

        return "Reject"

    # =====================================================
    # RECOMMENDATION
    # =====================================================

    def recommendation(

        self,

        overall,

        missing_skills

    ):

        if overall >= 90:

            return (

                "Excellent alignment with the Job Description. "

                "Resume is highly ATS optimized."

            )

        if overall >= 75:

            if missing_skills:

                return (

                    "Strong profile. Improve these skills: "

                    + ", ".join(missing_skills[:5])

                )

            return (

                "Strong profile with good ATS compatibility."

            )

        if overall >= 60:

            return (

                "Average match. Add more projects, measurable "

                "achievements and technical keywords."

            )

        return (

            "Resume requires significant improvement before "

            "applying for this role."

        )

    # =====================================================
    # COMPLETE ANALYSIS
    # =====================================================

    def analyze(

        self,

        resume,

        job

    ):

        similarity = self.similarity_score(

            resume,

            job

        )

        keyword = self.keyword_match(

            resume,

            job

        )

        skill_report = self.skill_match(

            resume,

            job

        )

        overall = self.overall_match(

            similarity,

            keyword,

            skill_report["Skill Coverage"]

        )

        ats = self.ats_score(

            overall

        )

        return {

            "Similarity Score": similarity,

            "Keyword Match": keyword,

            "Skill Coverage": skill_report["Skill Coverage"],

            "Overall Match": overall,

            "ATS Score": ats,

            "Resume Skills": skill_report["Resume Skills"],

            "Job Skills": skill_report["Job Skills"],

            "Matched Skills": skill_report["Matched Skills"],

            "Missing Skills": skill_report["Missing Skills"],

            "Grade": self.grade(overall),

            "Confidence": self.confidence(overall),

            "Hiring Status": self.hiring_status(overall),

            "Recruiter Decision": self.recruiter_decision(overall),

            "Recommendation": self.recommendation(

                overall,

                skill_report["Missing Skills"]

            )

        }