# app.py
import streamlit as st
from preprocess import load_pdf, clean_text
from vector_store import VectorStore
from qa import QASystem
import os

st.title("📚 RAG PDF 问答系统")

uploaded_file = st.file_uploader("上传 PDF 文件", type="pdf")

if uploaded_file:
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("PDF 上传成功!")

    text = clean_text(load_pdf(file_path))
    st.write("PDF 文本提取完成，正在构建向量索引...")
    
    store = VectorStore()
    store.add_documents([text])
    store.save()
    st.success("向量索引构建完成!")

    question = st.text_input("请输入你的问题")
    if question:
        qa_system = QASystem()
        answer = qa_system.answer(question)
        st.subheader("回答")
        st.write(answer)
