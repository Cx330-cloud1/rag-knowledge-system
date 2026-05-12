import streamlit as st
from pypdf import PdfReader

st.title("RAG知识库系统")

st.write("上传PDF并进行AI问答")

# 上传PDF
uploaded_file = st.file_uploader(
    "请上传PDF文件",
    type="pdf"
)

if uploaded_file is not None:

    st.success("PDF上传成功！")

    st.write("文件名：", uploaded_file.name)

    # 读取PDF
    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        content = page.extract_text()

        if content:
            text += content

    st.subheader("PDF读取完成")

    # 用户问题
    question = st.text_input("请输入你的问题")

    if question:

        st.subheader("AI回答")

        # 检索关键词
        if question in text:

            index = text.find(question)

            start = max(index - 300, 0)
            end = min(index + 800, len(text))

            result = text[start:end]

            # 模拟AI总结
            answer = f"""
根据文档内容：

文档中提到了“{question}”。

相关内容摘要：

{result}

系统分析：

该内容主要围绕“{question}”展开讨论，
说明它在文档中具有一定的重要性。
"""

            st.write(answer)

        else:

            st.warning("没有找到相关内容")