# preprocess.py
import os
from PyPDF2 import PdfReader

def load_pdf(file_path):
    """读取 PDF 并返回文本"""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def clean_text(text):
    """简单清洗文本"""
    return text.replace("\n", " ").strip()

if __name__ == "__main__":
    # 测试
    sample_pdf = "data/sample.pdf"
    text = load_pdf(sample_pdf)
    print(clean_text(text[:500]))
