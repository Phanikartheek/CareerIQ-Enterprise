"""
=========================================================
CareerIQ Enterprise
Enterprise AI Interview Generator
Author : Vellanki phanikartheek
Version : 9.0
=========================================================
"""

import random


class InterviewGenerator:

    def __init__(self):
        pass

    # --------------------------------------------------
    # Technical Questions
    # --------------------------------------------------

    def technical_questions(
        self,
        matched_skills,
        experience
    ):

        questions = []

        for skill in sorted(set(matched_skills)):

            questions.append(
                f"Explain the fundamentals of {skill}."
            )

            questions.append(
                f"Describe a real project where you used {skill}."
            )

            if experience >= 3:

                questions.append(
                    f"What are the best practices while working with {skill}?"
                )

            if experience >= 5:

                questions.append(
                    f"How would you architect an enterprise solution using {skill}?"
                )

        return questions

    # --------------------------------------------------
    # Missing Skills
    # --------------------------------------------------

    def missing_skill_questions(
        self,
        missing_skills
    ):

        return [

            f"If assigned a project requiring {skill}, how would you learn and implement it?"

            for skill in sorted(set(missing_skills))

        ]

    # --------------------------------------------------
    # Coding Questions
    # --------------------------------------------------

    def coding_questions(self):

        return [

            "Write a Python function to remove duplicate values from a list.",

            "Explain the difference between List, Tuple and Set.",

            "What is time complexity?",

            "Explain OOP concepts with examples.",

            "Difference between multithreading and multiprocessing.",

            "Explain REST API architecture."

        ]

    # --------------------------------------------------
    # Behavioural
    # --------------------------------------------------

    def behavioral_questions(self):

        return [

            "Tell us about a difficult project you handled.",

            "Describe a conflict in your team and how you resolved it.",

            "How do you prioritize multiple deadlines?",

            "Describe your leadership style.",

            "Tell us about a major failure and what you learned.",

            "How do you work under pressure?"

        ]

    # --------------------------------------------------
    # HR
    # --------------------------------------------------

    def hr_questions(self):

        return [

            "Tell me about yourself.",

            "Why should we hire you?",

            "Why are you leaving your current organization?",

            "Where do you see yourself in five years?",

            "What are your strengths?",

            "What is one weakness you are currently improving?"

        ]

    # --------------------------------------------------
    # Communication
    # --------------------------------------------------

    def communication_questions(self):

        return [

            "Explain a technical concept to a non-technical person.",

            "How would you present project progress to senior management?",

            "Describe a situation where communication prevented a project issue."

        ]

    # --------------------------------------------------
    # Interview Scorecard
    # --------------------------------------------------

    def scorecard(self):

        return {

            "Technical Skills": 30,

            "Problem Solving": 20,

            "Communication": 15,

            "Projects": 15,

            "Behaviour": 10,

            "Leadership": 10

        }

    # --------------------------------------------------
    # Generate Complete Interview Kit
    # --------------------------------------------------

    def generate(
        self,
        matched_skills,
        missing_skills,
        experience
    ):

        technical = self.technical_questions(
            matched_skills,
            experience
        )

        missing = self.missing_skill_questions(
            missing_skills
        )

        coding = self.coding_questions()

        behavioral = self.behavioral_questions()

        hr = self.hr_questions()

        communication = self.communication_questions()

        questions = (

            technical
            + missing
            + coding
            + behavioral
            + hr
            + communication

        )

        questions = list(dict.fromkeys(questions))

        random.shuffle(questions)

        return {

            "Questions": questions[:25],

            "Scorecard": self.scorecard(),

            "Total Questions": min(25, len(questions))

        }