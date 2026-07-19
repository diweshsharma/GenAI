from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct",
    task = 'text_generation'
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("what is the capital of India")

print(response.content)