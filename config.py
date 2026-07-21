from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings


llm = ChatMistralAI(model="mistral-medium-3-5")

embedding = MistralAIEmbeddings()
