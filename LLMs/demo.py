from dotenv import load_dotenv
from langchain_groq import ChatGroq
 
load_dotenv()


model = ChatGroq(model = "llama-3.3-70b-versatile")
 
response = model.invoke("In one sentence, what is LangChain useful for?")
print(response.content)

# I don't have free LLM api credits so i  use GRoq and there is no legacy LLM model in groq , so i use chatmodel 