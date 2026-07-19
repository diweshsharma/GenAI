from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

messages = [
    SystemMessage(content = 'you are a helpful assistant'),
    HumanMessage(content = 'Tell me about langchain')
]
response = model.invoke(messages)
messages.append(AIMessage(content = response.content))

print(messages)