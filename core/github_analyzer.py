"""
=========================================================
CareerIQ Enterprise
Enterprise GitHub Portfolio Analyzer Engine
Author : CareerIQ Engineering
Version : 11.0 Enterprise
=========================================================
"""

import re
import requests
from collections import Counter
from datetime import datetime


class GitHubAnalyzer:
    """
    Fetches, parses, and evaluates GitHub portfolios for tech recruitment intelligence.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self, token=None):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "CareerIQ-Portfolio-Analyzer"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"

    def clean_username(self, input_str: str) -> str:
        """
        Extract clean GitHub username from URL or username string.
        """
        input_str = input_str.strip()
        # If full URL like https://github.com/torvalds
        match = re.search(r"github\.com/([a-zA-Z0-9_\-]+)", input_str)
        if match:
            return match.group(1)
        # Remove any leading @ or slashes
        return input_str.lstrip("@/").strip()

    def fetch_user_data(self, username: str):
        """
        Fetch basic user profile info from GitHub API.
        """
        username = self.clean_username(username)
        if not username:
            return {"error": "Invalid GitHub username."}

        url = f"{self.BASE_URL}/users/{username}"
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            if resp.status_code == 404:
                return {"error": f"GitHub user '{username}' not found."}
            elif resp.status_code == 403:
                return {"error": "GitHub API rate limit reached. Try again shortly or supply a Personal Access Token in Settings."}
            elif resp.status_code != 200:
                return {"error": f"Failed to fetch user data (HTTP {resp.status_code})."}
            return resp.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Network error connecting to GitHub: {str(e)}"}

    def fetch_user_repos(self, username: str, max_repos: int = 100):
        """
        Fetch public repositories for the user.
        """
        username = self.clean_username(username)
        url = f"{self.BASE_URL}/users/{username}/repos?per_page={max_repos}&sort=updated"
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            if resp.status_code != 200:
                return []
            repos = resp.json()
            if isinstance(repos, list):
                return repos
            return []
        except Exception:
            return []

    def analyze_portfolio(self, username: str):
        """
        Runs comprehensive AI analysis on the GitHub user's profile and repositories.
        """
        user_info = self.fetch_user_data(username)
        if "error" in user_info:
            return user_info

        clean_user = user_info.get("login", username)
        repos = self.fetch_user_repos(clean_user)

        # Basic Stats
        total_repos = len(repos)
        public_repos_count = user_info.get("public_repos", total_repos)
        followers = user_info.get("followers", 0)
        following = user_info.get("following", 0)
        bio = user_info.get("bio") or "No bio provided"
        blog = user_info.get("blog") or ""
        company = user_info.get("company") or ""
        location = user_info.get("location") or "Not specified"
        created_at = user_info.get("created_at", "")

        account_age_years = 0
        if created_at:
            try:
                created_dt = datetime.strptime(created_at[:10], "%Y-%m-%d")
                account_age_years = round((datetime.now() - created_dt).days / 365.25, 1)
            except Exception:
                account_age_years = 1.0

        # Process Repositories
        total_stars = 0
        total_forks = 0
        total_open_issues = 0
        languages_list = []
        topics_list = []
        has_description_count = 0
        has_homepage_count = 0
        original_repos_count = 0

        repo_details = []
        for r in repos:
            is_fork = r.get("fork", False)
            if not is_fork:
                original_repos_count += 1

            stars = r.get("stargazers_count", 0)
            forks = r.get("forks_count", 0)
            issues = r.get("open_issues_count", 0)
            lang = r.get("language")
            desc = r.get("description")
            homepage = r.get("homepage")
            topics = r.get("topics", [])

            total_stars += stars
            total_forks += forks
            total_open_issues += issues

            if lang:
                languages_list.append(lang)
            if topics:
                topics_list.extend(topics)
            if desc:
                has_description_count += 1
            if homepage:
                has_homepage_count += 1

            repo_details.append({
                "name": r.get("name"),
                "description": desc or "No description provided",
                "stars": stars,
                "forks": forks,
                "language": lang or "Other",
                "url": r.get("html_url"),
                "is_fork": is_fork,
                "updated_at": (r.get("updated_at") or "")[:10],
                "topics": topics
            })

        # Sort repos by stars, then updated_at
        repo_details.sort(key=lambda x: (x["stars"], x["updated_at"]), reverse=True)

        # Language distribution
        lang_counts = Counter(languages_list)
        total_langs = len(languages_list)
        lang_distribution = {
            lang: round((count / total_langs) * 100, 1)
            for lang, count in lang_counts.most_common()
        } if total_langs > 0 else {}

        # Top Topics
        topic_counts = Counter(topics_list).most_common(10)

        # Developer Archetype Determination
        top_languages = [l.lower() for l in lang_counts.keys()]
        all_text = (bio + " " + " ".join(topics_list) + " " + " ".join([r["name"] for r in repo_details])).lower()

        archetypes = []
        if any(l in ["python", "r", "jupyter notebook"] for l in top_languages) or any(k in all_text for k in ["ml", "ai", "machine learning", "deep learning", "neural", "vision", "nlp", "llm"]):
            archetypes.append("AI / Machine Learning Engineer")
        if any(l in ["javascript", "typescript", "html", "css"] for l in top_languages) and any(l in ["python", "go", "java", "node", "php", "ruby", "c#"] for l in top_languages):
            archetypes.append("Full Stack Developer")
        elif any(l in ["javascript", "typescript", "html", "css"] for l in top_languages) or "react" in all_text or "vue" in all_text or "frontend" in all_text:
            archetypes.append("Frontend Engineer")
        elif any(l in ["python", "go", "java", "rust", "c++", "c#", "scala"] for l in top_languages):
            archetypes.append("Backend Engineer")
        if any(k in all_text for k in ["docker", "kubernetes", "ci/cd", "devops", "terraform", "ansible", "cloud"]):
            archetypes.append("DevOps / Cloud Specialist")

        if not archetypes:
            archetypes.append("Software Developer")

        # Portfolio Quality Scoring (0 - 100)
        score = 40  # base score for having an account

        # Points for repo quantity & originals
        if original_repos_count >= 5:
            score += 15
        elif original_repos_count >= 2:
            score += 10
        elif original_repos_count >= 1:
            score += 5

        # Points for descriptions & quality
        if total_repos > 0:
            desc_ratio = has_description_count / total_repos
            if desc_ratio >= 0.7:
                score += 15
            elif desc_ratio >= 0.4:
                score += 10
            else:
                score += 5

        # Points for stars & community engagement
        if total_stars >= 50:
            score += 15
        elif total_stars >= 10:
            score += 10
        elif total_stars >= 1:
            score += 5

        # Points for bio and links
        if bio and bio != "No bio provided":
            score += 5
        if blog:
            score += 5
        if followers >= 10:
            score += 5
        elif followers >= 2:
            score += 3

        portfolio_score = min(100, max(10, score))

        # Grade
        if portfolio_score >= 85:
            grade = "A+"
            status = "🌟 Exceptional Portfolio"
        elif portfolio_score >= 75:
            grade = "A"
            status = "🚀 High Impact Developer"
        elif portfolio_score >= 60:
            grade = "B"
            status = "👍 Solid Developer Presence"
        elif portfolio_score >= 45:
            grade = "C"
            status = "📈 Developing Portfolio"
        else:
            grade = "D"
            status = "⚠️ Needs Optimization"

        # Recommendations
        recommendations = []
        if total_repos == 0:
            recommendations.append("Upload your core project repositories to showcase your hands-on code.")
        if total_repos > 0 and (has_description_count / total_repos) < 0.7:
            recommendations.append("Add clear descriptions and README.md files to all repositories to improve recruiter readability.")
        if not bio or bio == "No bio provided":
            recommendations.append("Add a professional bio highlighting your target tech stack (e.g. AI/ML, Python, Full Stack).")
        if not blog:
            recommendations.append("Link your LinkedIn, personal portfolio website, or live deployed demos in your profile.")
        if has_homepage_count == 0:
            recommendations.append("Add live demo URLs in the 'Website' field of repository settings.")
        if len(topics_list) < 5:
            recommendations.append("Add topic tags (e.g., #fastapi, #machine-learning, #react) to your repositories for higher GitHub discoverability.")
        if len(recommendations) < 3:
            recommendations.append("Pin your top 4-6 most impressive original repositories to your GitHub profile overview.")
            recommendations.append("Add automated test workflows (GitHub Actions CI/CD) and badges in repository READMEs.")

        return {
            "username": clean_user,
            "name": user_info.get("name") or clean_user,
            "avatar_url": user_info.get("avatar_url"),
            "html_url": user_info.get("html_url"),
            "bio": bio,
            "company": company,
            "location": location,
            "blog": blog,
            "public_repos": public_repos_count,
            "total_repos_analyzed": total_repos,
            "original_repos": original_repos_count,
            "followers": followers,
            "following": following,
            "account_age_years": account_age_years,
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_open_issues": total_open_issues,
            "languages": lang_distribution,
            "top_topics": topic_counts,
            "archetypes": archetypes,
            "portfolio_score": portfolio_score,
            "grade": grade,
            "status": status,
            "recommendations": recommendations,
            "top_repos": repo_details[:10],
            "all_repos": repo_details
        }
