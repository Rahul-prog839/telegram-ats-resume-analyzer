import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ATSAnalyzer:

    def calculate_score(self, resume_text, jd_text):

        resume = resume_text.lower()
        jd = jd_text.lower()

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(
            [resume, jd]
        )

        similarity = cosine_similarity(
            vectors[0],
            vectors[1]
        )[0][0]

        score = round(similarity * 100, 2)

        return score