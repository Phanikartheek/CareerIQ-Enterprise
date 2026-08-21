"""
=========================================================
CareerIQ Enterprise
Universal AI Engine
Version : 10.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

from core.analytics import ResumeAnalytics
from core.ml_prediction import MLPredictor
from core.ats_engine import ATSEngine

# ------------------------------------------------------
# Optional Modules
# ------------------------------------------------------

try:
    from core.deep_learning import DeepLearningModel
    DL_AVAILABLE = True
except Exception:
    DL_AVAILABLE = False

try:
    from core.llm_engine import LLMEngine
    LLM_AVAILABLE = True
except Exception:
    LLM_AVAILABLE = False


class AIEngine:

    def __init__(self):

        # ==========================================
        # Core Engines
        # ==========================================

        self.ats = ATSEngine()

        self.analytics = ResumeAnalytics()

        self.ml = MLPredictor()

        self.dl = DeepLearningModel() if DL_AVAILABLE else None

        self.llm = LLMEngine() if LLM_AVAILABLE else None

    # =====================================================
    # ATS ENGINE
    # =====================================================

    def ats_report(
        self,
        parsed_resume,
        skill_database
    ):

        return self.ats.analyze(
            parsed_resume,
            skill_database
        )

    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    def ml_prediction(self, **kwargs):

        return self.ml.full_report(**kwargs)

    # =====================================================
    # DEEP LEARNING
    # =====================================================

    def dl_prediction(self, **kwargs):

        if self.dl is None:

            return {

                "Hiring Score": 0,

                "Grade": "-",

                "Hiring Status": "Unavailable",

                "Recommendation":
                    "Deep Learning module disabled."

            }

        return self.dl.full_report(**kwargs)

    # =====================================================
    # ANALYTICS
    # =====================================================

    def analytics_summary(
        self,
        features
    ):

        return self.analytics.summary(features)

    def dashboard_metrics(
        self,
        ats,
        similarity,
        quality
    ):

        return self.analytics.dashboard_metrics(
            ats,
            similarity,
            quality
        )

    # =====================================================
    # AI CAREER COACH
    # =====================================================

    def ai_review(

        self,

        ats,

        similarity,

        quality,

        experience,

        matched,

        missing

    ):

        if self.llm is None:

            return {

                "Executive Summary": "LLM Disabled",

                "AI Review": [

                    "LLM module not available."

                ],

                "Strengths": [],

                "Weaknesses": [],

                "Career Advice": [],

                "Recruiter Decision": "Unavailable",

                "Hiring Probability": 0

            }

        return self.llm.generate_report(

            ats=ats,

            similarity=similarity,

            quality=quality,

            experience=experience,

            matched=matched,

            missing=missing

        )

    # =====================================================
    # COMPLETE ENTERPRISE REPORT
    # =====================================================

    def enterprise_report(

        self,

        parsed_resume,

        skill_database,

        ats,

        similarity,

        quality,

        experience,

        matched,

        missing,

        ml_kwargs,

        dl_kwargs

    ):

        ats_result = self.ats_report(

            parsed_resume,

            skill_database

        )

        analytics = self.dashboard_metrics(

            ats,

            similarity,

            quality

        )

        ml = self.ml_prediction(

            **ml_kwargs

        )

        dl = self.dl_prediction(

            **dl_kwargs

        )

        ai = self.ai_review(

            ats,

            similarity,

            quality,

            experience,

            matched,

            missing

        )

        return {

            "ATS": ats_result,

            "Analytics": analytics,

            "Machine Learning": ml,

            "Deep Learning": dl,

            "AI Review": ai

        }

    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    def system_status(self):

        return {

            "ATS Engine": True,

            "Analytics": True,

            "Machine Learning": True,

            "Deep Learning": DL_AVAILABLE,

            "LLM Engine": LLM_AVAILABLE

        }

    # =====================================================
    # VERSION
    # =====================================================

    def version(self):

        return {

            "Platform": "CareerIQ",

            "Version": "12.0 Enterprise"

        }