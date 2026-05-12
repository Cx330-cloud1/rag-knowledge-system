# qa.py
from vector_store import VectorStore

class QASystem:
    def __init__(self, vector_store_path="vector_store.pkl"):
        self.store = VectorStore.load(vector_store_path)

    def answer(self, question):
        top_docs = self.store.search(question)
        # 简单返回最相似文档内容
        answer_text = "\n".join([doc for doc, score in top_docs])
        return answer_text
