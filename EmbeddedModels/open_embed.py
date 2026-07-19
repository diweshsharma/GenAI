from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

text = 'what is the capital of India'

vector = llm.embed_query(text)
print(str(vector))