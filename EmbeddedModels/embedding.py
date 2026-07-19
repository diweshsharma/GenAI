from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

embeddings = OpenAIEmbeddings(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    model="nomic-embed-text-v1_5",
)

vector = embeddings.embed_query("What is LangChain?")
print(str(vector))


#this will not work