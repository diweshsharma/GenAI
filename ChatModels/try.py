from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
 
load_dotenv()

MODEL = "google_genai:gemini-3.5-flash"

model = init_chat_model(MODEL, temperature=0.7)
 
response = model.invoke("Gives name of free chatmodels")
# print(response.response_metadata)
print(response.text)