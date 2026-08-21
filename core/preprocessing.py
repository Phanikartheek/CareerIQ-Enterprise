"""
=========================================================
Resume Intelligence AI
Text Preprocessing Engine
Author : Vellanki phanikartheek
Version : 5.0
=========================================================
"""

import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download once if missing
try:
    stop_words = set(stopwords.words("english"))
except:
    nltk.download("stopwords")
    nltk.download("punkt")
    nltk.download("wordnet")
    nltk.download("omw-1.4")
    stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


class TextPreprocessor:

    def __init__(self):
        pass

    # ---------------------------------

    def lowercase(self, text):

        return text.lower()

    # ---------------------------------

    def remove_urls(self, text):

        return re.sub(r"http\S+|www\S+", "", text)

    # ---------------------------------

    def remove_email(self, text):

        return re.sub(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}",
            "",
            text
        )

    # ---------------------------------

    def remove_phone(self, text):

        return re.sub(r"\+?\d[\d\s\-]{8,15}", "", text)

    # ---------------------------------

    def remove_numbers(self, text):

        return re.sub(r"\d+", " ", text)

    # ---------------------------------

    def remove_special_characters(self, text):

        return re.sub(r"[^a-zA-Z\s]", " ", text)

    # ---------------------------------

    def remove_punctuation(self, text):

        return text.translate(
            str.maketrans("", "", string.punctuation)
        )

    # ---------------------------------

    def remove_extra_spaces(self, text):

        return re.sub(r"\s+", " ", text).strip()

    # ---------------------------------

    def tokenize(self, text):

        return word_tokenize(text)

    # ---------------------------------

    def remove_stopwords(self, tokens):

        return [
            word
            for word in tokens
            if word not in stop_words
        ]

    # ---------------------------------

    def lemmatize(self, tokens):

        return [
            lemmatizer.lemmatize(word)
            for word in tokens
        ]

    # ---------------------------------

    def keyword_frequency(self, tokens):

        freq = {}

        for word in tokens:

            freq[word] = freq.get(word, 0) + 1

        return dict(
            sorted(
                freq.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )

    # ---------------------------------

    def unique_words(self, tokens):

        return len(set(tokens))

    # ---------------------------------

    def vocabulary_richness(self, tokens):

        if len(tokens) == 0:
            return 0

        return round(
            len(set(tokens)) / len(tokens),
            2
        )

    # ---------------------------------

    def preprocess(self, text):

        text = self.lowercase(text)

        text = self.remove_urls(text)

        text = self.remove_email(text)

        text = self.remove_phone(text)

        text = self.remove_numbers(text)

        text = self.remove_special_characters(text)

        text = self.remove_punctuation(text)

        text = self.remove_extra_spaces(text)

        tokens = self.tokenize(text)

        tokens = self.remove_stopwords(tokens)

        tokens = self.lemmatize(tokens)

        clean_text = " ".join(tokens)

        analysis = {

            "clean_text": clean_text,

            "tokens": tokens,

            "total_words": len(tokens),

            "unique_words": self.unique_words(tokens),

            "vocabulary_richness": self.vocabulary_richness(tokens),

            "top_keywords": list(
                self.keyword_frequency(tokens).items()
            )[:20]

        }

        return analysis