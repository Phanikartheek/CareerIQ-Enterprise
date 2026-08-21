import pandas as pd


class RecruiterDashboard:

    def __init__(self):

        self.candidates = []

    def add_candidate(

        self,

        name,

        department,

        role,

        ats,

        similarity,

        quality,

        hiring,

        experience

    ):

        self.candidates.append({

            "Candidate": name,

            "Department": department,

            "Role": role,

            "ATS Score": ats,

            "Similarity": similarity,

            "Resume Quality": quality,

            "Hiring Score": hiring,

            "Experience": experience

        })

    def ranking(self):

        df = pd.DataFrame(self.candidates)

        if df.empty:

            return df

        df = df.sort_values(

            by="Hiring Score",

            ascending=False

        )

        df.reset_index(drop=True, inplace=True)

        df.index += 1

        return df

    def top_candidate(self):

        df = self.ranking()

        if df.empty:

            return None

        return df.iloc[0]