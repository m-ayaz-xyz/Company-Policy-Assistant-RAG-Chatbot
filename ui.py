import streamlit as st
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from config import llm, embedding


st.set_page_config(
    page_title="Company Policy Assistant",
    page_icon="📄",
    layout="wide"
)


st.title("Company Policy Assistant")

st.write(
    "Upload your company policy PDF and ask questions."
)


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload Policy PDF",
    type=["pdf"]
)


if uploaded_file:

    if "vectorstore" not in st.session_state:

        with st.spinner("Processing PDF..."):

            # Save temporary PDF

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            )

            temp_file.write(
                uploaded_file.read()
            )

            temp_file.close()


            # Load PDF

            loader = PyPDFLoader(
                temp_file.name
            )

            documents = loader.load()


            # Split

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(
                documents
            )


            # Create Chroma DB

            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embedding,
                persist_directory="./chroma_db"
            )


            st.session_state.vectorstore = vectorstore


            os.remove(
                temp_file.name
            )


        st.success(
            "PDF processed successfully!"
        )


# Question Answering
if "vectorstore" in st.session_state:


    retriever = (
        st.session_state.vectorstore
        .as_retriever(
            search_kwargs={
                "k":3
            }
        )
    )


    def format_docs(docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )


    prompt = ChatPromptTemplate.from_template(
        """
        You are a company policy assistant.

        Answer only from the given context.

        If answer is not available,
        say "I don't know".

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
        }
        | prompt
        | llm
        | StrOutputParser()
    )


    st.divider()


    question = st.text_input(
        "Ask your question"
    )


    if st.button("Ask"):

        if question:

            with st.spinner("Thinking..."):

                answer = chain.invoke(
                    question
                )


            st.subheader(
                "Answer"
            )

            st.write(
                answer
            )

