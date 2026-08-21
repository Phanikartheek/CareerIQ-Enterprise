"""
=========================================================
CareerIQ Enterprise
Enterprise Resume Parser
Version : 10.1 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import re
import pdfplumber
import docx

from core.keyword_engine import KeywordEngine
from core.ats_engine import ATSEngine


class ResumeParser:

    def __init__(self):

        self.keyword_engine = KeywordEngine()
        self.ats_engine = ATSEngine()

    # =====================================================
    # TEXT EXTRACTION
    # =====================================================

    def extract_text(self, uploaded_file):

        filename = uploaded_file.name.lower()

        text = ""

        if filename.endswith(".pdf"):

            with pdfplumber.open(uploaded_file) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text + "\n"

        elif filename.endswith(".docx"):

            document = docx.Document(uploaded_file)

            text = "\n".join(

                paragraph.text

                for paragraph in document.paragraphs

            )

        return text.strip()

    # =====================================================
    # CONTACT INFORMATION
    # =====================================================

    def extract_email(self, text):

        match = re.search(

            r'[\w\.-]+@[\w\.-]+\.\w+',

            text

        )

        return match.group(0) if match else ""

    def extract_phone(self, text):

        match = re.search(

            r'(\+91[\-\s]?)?[6-9]\d{9}',

            text

        )

        return match.group(0) if match else ""

    def extract_linkedin(self, text):

        match = re.search(

            r'https?://(www\.)?linkedin\.com/\S+',

            text

        )

        return match.group(0) if match else ""

    def extract_github(self, text):

        match = re.search(

            r'https?://(www\.)?github\.com/\S+',

            text

        )

        return match.group(0) if match else ""
    # =====================================================
    # PORTFOLIO LINKS
    # =====================================================

    def extract_portfolio(self, text):

        websites = re.findall(

            r'https?://[^\s]+',

            text

        )

        portfolio = []

        for site in websites:

            lower = site.lower()

            if "linkedin" in lower:

                continue

            if "github" in lower:

                continue

            portfolio.append(site)

        return list(set(portfolio))

    # =====================================================
    # SKILLS
    # =====================================================

    def extract_skills(self, text):

        return self.keyword_engine.extract_skills(text)

    # =====================================================
    # EXPERIENCE
    # =====================================================

    def extract_experience(self, text):

        matches = re.findall(

            r'(\d+)\+?\s*(years|year|yrs|yr)',

            text.lower()

        )

        if not matches:

            return 0

        years = [

            int(match[0])

            for match in matches

        ]

        return max(years)

    # =====================================================
    # EDUCATION
    # =====================================================

    def extract_education(self, text):

        degrees = [
            "PhD",
            "Doctorate",
            "M.Tech",
            "MBA",
            "MCA",
            "M.Sc",
            "B.Tech",
            "B.E",
            "BCA",
            "B.Sc",
            "Diploma"
        ]

        found = []
        lines = text.splitlines()

        # Try to find the Education section first
        edu_section_text = ""
        in_edu_section = False
        section_headers = re.compile(
            r'^(education|qualification|academic|degree)',
            re.IGNORECASE
        )
        end_section_headers = re.compile(
            r'^(experience|skills|projects|certifications|work|employment|internship|objective|summary|profile)',
            re.IGNORECASE
        )

        for line in lines:
            stripped = line.strip()
            if section_headers.match(stripped):
                in_edu_section = True
                continue
            if in_edu_section:
                if end_section_headers.match(stripped) and stripped:
                    break
                edu_section_text += " " + stripped

        # Search in education section text first; fallback to full text
        search_text = edu_section_text if edu_section_text.strip() else text
        search_lower = search_text.lower()

        for degree in degrees:
            if degree.lower() in search_lower:
                found.append(degree)

        return found

    # =====================================================
    # PROJECTS
    # =====================================================

    def extract_projects(self, text):
        """
        Robust project counter tuned for real resume formats.
        """
        lines = text.splitlines()

        in_projects = False
        project_lines = []

        # Matches section headers like: PROJECTS, Projects, Projects:
        # but NOT a one-word subtitle like "Project" that appears under a title
        section_start = re.compile(
            r'^\s*(PROJECTS|projects?\s*[\:\-]?|personal\s+projects?|key\s+projects?|'
            r'academic\s+projects?|project\s+experience|notable\s+projects?)\s*$',
            re.IGNORECASE
        )

        # A "subtitle" like "Personal Portfolio Project" or "Self Initiated Project"
        # should NOT reset the section
        single_project_word = re.compile(r'^\s*project\s*$', re.IGNORECASE)

        # Section end — match both Title Case and ALL CAPS (with or without colon)
        section_end = re.compile(
            r'^\s*(EDUCATION|SKILLS?|CERTIFICATIONS?|EXPERIENCE|WORK\s+EXPERIENCE|'
            r'EMPLOYMENT|INTERNSHIP|OBJECTIVE|SUMMARY|AWARDS?|ACHIEVEMENTS?|'
            r'PUBLICATIONS?|REFERENCES?|DECLARATION|'
            r'education|skills?|certifications?|experience|work\s+experience|'
            r'employment|internship|objective|summary|awards?|achievements?|'
            r'publications?|references?|declaration)\s*[:\-]?\s*$',
            re.IGNORECASE
        )

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            # Skip re-triggering section start on words like bare "Project"
            if single_project_word.match(stripped):
                if in_projects:
                    continue  # it's a subtitle, stay in section
            if section_start.match(stripped) and not in_projects:
                in_projects = True
                continue
            if in_projects:
                if section_end.match(stripped):
                    break
                project_lines.append(stripped)

        if project_lines:
            # Count project title lines: they end with a date range or are short
            # Pattern: "Project Name | Live Demo Jan 2025 – Dec 2025"
            title_with_date = re.compile(
                r'.+\|\s*(Live Demo|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|20\d\d)',
                re.IGNORECASE
            )
            bullet = re.compile(r'^[\d]+[.\)]\s+\S|^[•*▪▸➤✦◆\ufffd]\s*\S')

            count = 0
            for l in project_lines:
                words = l.split()
                # Title line with date = definitely a project entry
                if title_with_date.match(l):
                    count += 1
                # Short non-bullet line with no numbers = project title
                elif (len(words) <= 8
                      and not bullet.match(l)
                      and not any(c.isdigit() for c in l[:3])):
                    # Must start uppercase and contain no special chars
                    if l[0].isupper():
                        count += 1

            if count > 0:
                return count

            # Fallback: ~1 project per 5 lines
            return max(1, round(len(project_lines) / 5))

        # No section found — minimal fallback
        raw = text.lower().count("project")
        return max(1, min(raw, 1))



    # =====================================================
    # NAME
    # =====================================================

    def extract_name(self, text):

        lines = [

            line.strip()

            for line in text.splitlines()

            if line.strip()

        ]

        for line in lines[:5]:

            words = line.split()

            if 2 <= len(words) <= 4:

                if not any(char.isdigit() for char in line):

                    return line

        return "Unknown Candidate"

    # =====================================================
    # READING TIME
    # =====================================================

    def reading_time(self, text):

        words = len(text.split())

        return max(1, round(words / 200))
    # =====================================================
    # RESUME SCORE
    # =====================================================

    def resume_score(self, text):

        score = 50

        if self.extract_email(text):
            score += 10

        if self.extract_phone(text):
            score += 10

        if self.extract_linkedin(text):
            score += 5

        if self.extract_github(text):
            score += 5

        keyword_report = self.keyword_engine.analyze(text)
        skills = keyword_report["Skills"]

        score += min(len(skills) * 2, 20)

        experience = self.extract_experience(text)

        if experience >= 5:
            score += 5

        elif experience >= 2:
            score += 3

        education = self.extract_education(text)

        if education:
            score += 5

        return min(score, 100)

    # =====================================================
    # COMPLETE ANALYSIS
    # =====================================================

    def analyze(self, uploaded_file):
        """Extract resume details and produce a complete analysis result."""
        text = self.extract_text(uploaded_file)
        skills = self.extract_skills(text)
        parsed_resume = {
            "raw_text": text,
            "word_count": len(text.split()),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "linkedin": self.extract_linkedin(text),
            "github": self.extract_github(text),
        }
        ats_report = self.ats_engine.analyze(
            parsed_resume,
            self.keyword_engine.master_skills,
        )
        return {
            "raw_text": text,
            "name": self.extract_name(text),
            "email": parsed_resume["email"],
            "phone": parsed_resume["phone"],
            "linkedin": parsed_resume["linkedin"],
            "github": parsed_resume["github"],
            "portfolio": self.extract_portfolio(text),
            "skills": skills,
            "experience": self.extract_experience(text),
            "education": self.extract_education(text),
            "projects": self.extract_projects(text),
            "resume_score": self.resume_score(text),
            "reading_time": self.reading_time(text),
            "word_count": len(text.split()),
            "character_count": len(text),
            "line_count": len(text.splitlines()),
            "ats_analysis": ats_report,
        }
