# vector_store.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class VectorStore:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = None
        self.documents = []

    def add_documents(self, docs):
        self.documents.extend(docs)
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_k=3):
        query_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(query_vec, self.doc_vectors).flatten()
        indices = sims.argsort()[-top_k:][::-1]
        return [(self.documents[i], sims[i]) for i in indices]

    def save(self, file_path="vector_store.pkl"):
        with open(file_path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(file_path="vector_store.pkl"):
        with open(file_path, "rb") as f:
            return pickle.load(f)
