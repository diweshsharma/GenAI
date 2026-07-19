from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key , temperature = 1.5
)
chat_history = []
sys_prompt= "You are a big flirt and yor are talking to your girlfriend , when she gaves any input {user_input} you have to reply back in a flirty way make sure you don't go below the belt and not offend her at all , make sure strictly that you talk in simple language and not beat around the bush"
while(True):
    user_input = input('You: ')
    messages = [sys_prompt , user_input]
    chat_history.append(messages)
    
    if( user_input == 'exit'):
        break
    response = model.invoke(messages)
    chat_history.append(response.content)
    
    print(f" AI :{response.content}")