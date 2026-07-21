from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough

from config import llm
from config import embedding


db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

retriever = db.as_retriever(
    search_kwargs={"k":3}
)


def format_docs(docs):

    return "\n\n".join(doc.page_content for doc in docs)


prompt = ChatPromptTemplate.from_template(
"""
You are a HR assistant.

Answer only using the company policy.

If answer is not available, say

"I don't know."

Context:

{context}

Question:

{question}

Answer:
"""
)


chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    } | prompt| llm | StrOutputParser()
)
