"""
=========================================================
CareerIQ Enterprise
Enterprise LLM Engine
Version : 10.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

from datetime import datetime


class LLMEngine:

    def __init__(self):
        pass

    # ======================================================
    # Resume Review
    # ======================================================

    def review_resume(
        self,
        ats,
        similarity,
        quality,
        experience,
        matched,
        missing,
    ):

        review = []

        if ats >= 90:
            review.append("Excellent ATS optimization.")
        elif ats >= 75:
            review.append("Good ATS optimization.")
        else:
            review.append("Improve ATS keywords.")

        if similarity >= 85:
            review.append("Excellent Job Description Match.")
        elif similarity >= 70:
            review.append("Good Job Match.")
        else:
            review.append("Resume needs better JD alignment.")

        if quality >= 85:
            review.append("Professional Resume Formatting.")
        else:
            review.append("Improve formatting and readability.")

        if experience < 2:
            review.append("Add internships and practical projects.")
        elif experience < 5:
            review.append("Highlight measurable achievements.")
        else:
            review.append("Show leadership and business impact.")

        if missing:
            review.append(
                "Missing Skills: " + ", ".join(missing[:5])
            )

        return review

    # ======================================================
    # Strengths
    # ======================================================

    def strengths(self, matched):

        if not matched:
            return ["No strengths detected."]

        return [
            f"Strong knowledge of {skill}"
            for skill in matched
        ]

    # ======================================================
    # Weaknesses
    # ======================================================

    def weaknesses(self, missing):

        if not missing:
            return ["No major weaknesses detected."]

        return [
            f"Need improvement in {skill}"
            for skill in missing
        ]

    # ======================================================
    # Learning Plan
    # ======================================================

    def learning_plan(self, missing):

        if not missing:

            return [

                "Continue solving interview problems.",

                "Build portfolio projects.",

                "Maintain LinkedIn profile."

            ]

        plan = []

        for skill in missing:
            plan.append(f"Learn {skill}")

        plan.append("Build one production-level project.")
        plan.append("Update Resume after learning.")
        plan.append("Practice Mock Interviews.")

        return plan

    # ======================================================
    # Recruiter Decision
    # ======================================================

    def recruiter_feedback(self, score):

        if score >= 90:
            return "Highly Recommended"

        elif score >= 75:
            return "Recommended"

        elif score >= 60:
            return "Consider After Review"

        return "Not Recommended"

    # ======================================================
    # Executive Summary
    # ======================================================

    def executive_summary(
        self,
        ats,
        similarity,
        quality,
    ):

        overall = round(
            (ats + similarity + quality) / 3,
            2,
        )

        return f"""
Overall Resume Score : {overall}%

ATS Score : {ats}%

Job Similarity : {similarity}%

Resume Quality : {quality}%
"""

    # ======================================================
    # Career Advice
    # ======================================================

    def career_advice(
        self,
        experience,
        missing,
    ):

        advice = []

        if experience < 2:
            advice.append(
                "Focus on internships and real-world projects."
            )

        elif experience < 5:
            advice.append(
                "Earn cloud and AI certifications."
            )

        else:
            advice.append(
                "Develop leadership skills."
            )

        if missing:
            advice.append(
                "Prioritize learning: "
                + ", ".join(missing[:5])
            )

        advice.append(
            "Maintain an updated LinkedIn and GitHub profile."
        )

        return advice

    # ======================================================
    # MAIN REPORT
    # ======================================================

    def generate_report(
        self,
        ats,
        similarity,
        quality,
        experience,
        matched,
        missing,
    ):

        overall = round(
            (ats + similarity + quality) / 3,
            2,
        )

        return {

            "Executive Summary":
                self.executive_summary(
                    ats,
                    similarity,
                    quality,
                ),

            "Overall Score":
                overall,

            "AI Review":
                self.review_resume(
                    ats,
                    similarity,
                    quality,
                    experience,
                    matched,
                    missing,
                ),

            "Strengths":
                self.strengths(
                    matched
                ),

            "Weaknesses":
                self.weaknesses(
                    missing
                ),

            "Learning Plan":
                self.learning_plan(
                    missing
                ),

            "Career Advice":
                self.career_advice(
                    experience,
                    missing,
                ),

            "Recruiter Decision":
                self.recruiter_feedback(
                    overall
                ),

            "Generated On":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )
        }

    # ======================================================
    # Backward Compatibility
    # ======================================================

    def generate(
        self,
        ats,
        similarity,
        quality,
        experience,
        matched,
        missing,
    ):

        return self.generate_report(
            ats,
            similarity,
            quality,
            experience,
            matched,
            missing,
        )