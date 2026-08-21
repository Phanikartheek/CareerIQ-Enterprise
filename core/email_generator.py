"""
=========================================================
CareerIQ Enterprise
Enterprise Professional Email Generator
Author : Vellanki phanikartheek
Version : 9.0
=========================================================
"""

from datetime import datetime


class EmailGenerator:

    def __init__(self):

        self.today = datetime.now().strftime("%d %B %Y")

    # --------------------------------------------------
    # Signature
    # --------------------------------------------------

    def signature(

        self,

        candidate_name

    ):

        return f"""

Kind Regards,

{candidate_name}

Generated using CareerIQ Career Intelligence Platform
"""

    # --------------------------------------------------
    # Job Application
    # --------------------------------------------------

    def application_email(

        self,

        candidate_name,

        company,

        role

    ):

        return f"""
Subject: Application for {role}

Dear Hiring Manager,

I hope you are doing well.

I am writing to apply for the position of {role} at {company}.

My experience includes Python, SQL, Machine Learning, Artificial Intelligence, Data Analytics, and end-to-end project development.

I have attached my resume for your review.

I would appreciate the opportunity to discuss how I can contribute to your team.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Follow Up
    # --------------------------------------------------

    def followup_email(

        self,

        candidate_name,

        company,

        role

    ):

        return f"""
Subject: Follow-up Regarding {role} Application

Dear Hiring Manager,

I hope you are doing well.

I wanted to politely follow up regarding my application for the {role} position at {company}.

I remain highly interested in joining your organization.

Thank you for your time and consideration.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Interview Thank You
    # --------------------------------------------------

    def thankyou_email(

        self,

        candidate_name,

        interviewer,

        company,

        role

    ):

        return f"""
Subject: Thank You for the Interview

Dear {interviewer},

Thank you for taking the time to interview me for the {role} position at {company}.

I enjoyed discussing the opportunity and learning more about your team.

I appreciate your consideration.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Interview Acceptance
    # --------------------------------------------------

    def interview_acceptance(

        self,

        candidate_name,

        company,

        interview_date

    ):

        return f"""
Subject: Interview Confirmation

Dear Hiring Team,

Thank you for inviting me to interview with {company}.

I am pleased to confirm my availability on {interview_date}.

I look forward to meeting your team.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Offer Acceptance
    # --------------------------------------------------

    def offer_acceptance(

        self,

        candidate_name,

        company,

        role

    ):

        return f"""
Subject: Acceptance of Offer - {role}

Dear Hiring Manager,

Thank you for offering me the role of {role} at {company}.

I am delighted to accept the offer and look forward to joining your organization.

Thank you once again.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Offer Decline
    # --------------------------------------------------

    def offer_decline(

        self,

        candidate_name,

        company,

        role

    ):

        return f"""
Subject: Offer for {role}

Dear Hiring Manager,

Thank you very much for offering me the position of {role}.

After careful consideration, I have decided not to accept the offer.

I sincerely appreciate the opportunity and wish {company} continued success.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Internship Application
    # --------------------------------------------------

    def internship_email(

        self,

        candidate_name,

        company

    ):

        return f"""
Subject: Internship Application

Dear Hiring Manager,

I am writing to express my interest in internship opportunities at {company}.

I am currently building practical experience in Python, Machine Learning, AI, and Data Analytics through real-world projects.

I would be grateful for an opportunity to contribute and learn.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Resignation Email
    # --------------------------------------------------

    def resignation_email(

        self,

        candidate_name,

        company

    ):

        return f"""
Subject: Resignation

Dear Manager,

Please accept this email as my formal resignation from {company}.

I sincerely appreciate the opportunities and support provided during my tenure.

Thank you for everything.

{self.signature(candidate_name)}
"""

    # --------------------------------------------------
    # Generic Generator
    # --------------------------------------------------

    def generate(

        self,

        email_type,

        **kwargs

    ):

        templates = {

            "application": self.application_email,

            "followup": self.followup_email,

            "thankyou": self.thankyou_email,

            "acceptance": self.interview_acceptance,

            "offer_acceptance": self.offer_acceptance,

            "offer_decline": self.offer_decline,

            "internship": self.internship_email,

            "resignation": self.resignation_email

        }

        if email_type not in templates:

            raise ValueError("Invalid email type.")

        return templates[email_type](**kwargs)