from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from config import embedding

loader = PyPDFLoader("upload/company_policy.pdf")

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)

db = Chroma.from_documents(
    docs,
    embedding=embedding,
    persist_directory="chroma_db"
)

print("PDF loaded Succesfully in ChromaDB")
