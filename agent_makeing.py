from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import requests
from langchain.tools import tool

from langchain_community.tools import DuckDuckGoSearchRun

llm = init_chat_model("groq:openai/gpt-oss-120b")
# print(search.invoke('what is the hot topic today in world'))

from langchain.agents import create_agent 
tooling = [DuckDuckGoSearchRun()]

agent = create_agent(
    model = llm,
    tools = tooling
    
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "what is the name of current Education minister of India"}
    ]
})
print(result['messages'][-1].content)