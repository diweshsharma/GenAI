# import langchain 

# print(langchain.__version__)

from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# import requests

# response = requests.post(
#     "https://openrouter.ai/api/v1/chat/completions",
#     headers={"Authorization": f"Bearer {api_key}"},
#     json={
#         "model": "openai/gpt-oss-20b:free",
#         "messages": [{"role": "user", "content": "Say hi in 5 words"}]
#     }
# )
# print(response.json()["choices"][0]["message"]["content"])

