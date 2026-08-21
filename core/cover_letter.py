"""
=========================================================
CareerIQ Enterprise
Enterprise AI Cover Letter Generator
Author : Vellanki phanikartheek
Version : 9.0
=========================================================
"""

from datetime import datetime


class CoverLetterGenerator:

    def __init__(self):

        self.today = datetime.today().strftime("%d %B %Y")

    # --------------------------------------------------
    # Closing
    # --------------------------------------------------

    def closing(

        self,

        candidate_name

    ):

        return f"""

Thank you for considering my application.

I look forward to discussing how I can contribute to your organization.

Sincerely,

{candidate_name}
"""

    # --------------------------------------------------
    # Professional Cover Letter
    # --------------------------------------------------

    def professional(

        self,

        candidate_name,

        company,

        department,

        role,

        experience,

        matched_skills,

        projects

    ):

        skills = ", ".join(matched_skills[:8])

        return f"""
Date: {self.today}

Hiring Manager
{company}

Subject: Application for {role}

Dear Hiring Manager,

I am writing to express my interest in the position of {role} within your {department} department.

With over {experience} years of professional experience, I have developed strong expertise in {skills} while delivering business-focused technical solutions.

During my career I have completed approximately {projects} projects involving analytics, automation, machine learning, and artificial intelligence.

I enjoy solving real-world business problems through technology and continuously improving my technical capabilities.

{self.closing(candidate_name)}
"""

    # --------------------------------------------------
    # Fresher Template
    # --------------------------------------------------

    def fresher(

        self,

        candidate_name,

        company,

        department,

        role,

        matched_skills,

        projects

    ):

        skills = ", ".join(matched_skills[:8])

        return f"""
Date: {self.today}

Hiring Manager
{company}

Subject: Application for {role}

Dear Hiring Manager,

I am excited to apply for the {role} position in your {department} department.

Although I am beginning my professional career, I have developed practical knowledge in {skills} through academic work and approximately {projects} hands-on projects.

I am eager to learn, contribute, and grow within your organization.

{self.closing(candidate_name)}
"""

    # --------------------------------------------------
    # Internship Template
    # --------------------------------------------------

    def internship(

        self,

        candidate_name,

        company,

        role,

        matched_skills

    ):

        skills = ", ".join(matched_skills[:6])

        return f"""
Date: {self.today}

Hiring Manager
{company}

Subject: Internship Application

Dear Hiring Manager,

I would like to apply for an internship opportunity as a {role}.

My current skills include {skills}, and I have been strengthening them through practical projects and continuous learning.

I would greatly appreciate an opportunity to contribute while learning from your experienced team.

{self.closing(candidate_name)}
"""

    # --------------------------------------------------
    # Executive Template
    # --------------------------------------------------

    def executive(

        self,

        candidate_name,

        company,

        department,

        role,

        experience

    ):

        return f"""
Date: {self.today}

Hiring Manager
{company}

Subject: Executive Application - {role}

Dear Hiring Manager,

With more than {experience} years of leadership experience, I have successfully delivered strategic initiatives, led cross-functional teams, and driven operational excellence.

I believe my leadership, technical expertise, and business-focused approach align well with your organization's objectives.

{self.closing(candidate_name)}
"""

    # --------------------------------------------------
    # Generate Cover Letter
    # --------------------------------------------------

    def generate(

        self,

        candidate_name,

        company,

        department,

        role,

        experience,

        matched_skills,

        projects

    ):

        if experience <= 1:

            return self.fresher(

                candidate_name,

                company,

                department,

                role,

                matched_skills,

                projects

            )

        elif experience >= 10:

            return self.executive(

                candidate_name,

                company,

                department,

                role,

                experience

            )

        else:

            return self.professional(

                candidate_name,

                company,

                department,

                role,

                experience,

                matched_skills,

                projects

            )