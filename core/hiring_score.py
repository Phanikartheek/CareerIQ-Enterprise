"""
=========================================================
CareerIQ Enterprise
Enterprise Hiring Score Engine
Version : 11.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""


class HiringScoreEngine:

    def __init__(self):

        self.weights = {

            "ATS": 0.25,

            "Similarity": 0.20,

            "Machine Learning": 0.15,

            "Deep Learning": 0.15,

            "Technical": 0.10,

            "Soft Skills": 0.05,

            "Experience": 0.10

        }

    # =====================================================
    # Normalize
    # =====================================================

    def normalize(self, value):

        if value is None:
            return 0

        value = float(value)

        if value < 0:
            value = 0

        if value > 100:
            value = 100

        return value

    # =====================================================
    # Final Score
    # =====================================================

    def calculate(

        self,

        ats,

        similarity,

        ml,

        dl,

        technical,

        soft_skills,

        experience

    ):

        ats = self.normalize(ats)

        similarity = self.normalize(similarity)

        ml = self.normalize(ml)

        dl = self.normalize(dl)

        technical = self.normalize(technical)

        soft_skills = self.normalize(soft_skills)

        experience = self.normalize(experience)

        final_score = (

            ats * self.weights["ATS"]

            +

            similarity * self.weights["Similarity"]

            +

            ml * self.weights["Machine Learning"]

            +

            dl * self.weights["Deep Learning"]

            +

            technical * self.weights["Technical"]

            +

            soft_skills * self.weights["Soft Skills"]

            +

            experience * self.weights["Experience"]

        )

        final_score = round(final_score, 2)

        return final_score

    # =====================================================
    # Grade
    # =====================================================

    def grade(self, score):

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
    # Recommendation
    # =====================================================

    def recommendation(self, score):

        if score >= 95:

            return "Outstanding Candidate"

        elif score >= 85:

            return "Highly Recommended"

        elif score >= 75:

            return "Recommended"

        elif score >= 60:

            return "Consider After Review"

        return "Not Recommended"

    # =====================================================
    # Risk Level
    # =====================================================

    def risk(self, score):

        if score >= 85:

            return "Low"

        elif score >= 70:

            return "Medium"

        return "High"

    # =====================================================
    # Hiring Probability
    # =====================================================

    def hiring_probability(self, score):

        return round(min(score * 1.05, 100), 2)

    # =====================================================
    # Complete Report
    # =====================================================

    def report(

        self,

        ats,

        similarity,

        ml,

        dl,

        technical,

        soft_skills,

        experience

    ):

        score = self.calculate(

            ats,

            similarity,

            ml,

            dl,

            technical,

            soft_skills,

            experience

        )

        return {

            "Hiring Score": score,

            "Grade": self.grade(score),

            "Recommendation": self.recommendation(score),

            "Risk": self.risk(score),

            "Hiring Probability": self.hiring_probability(score)

        }