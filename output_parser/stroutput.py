from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
load_dotenv()

api_key = os.getenv('OPENROUTER_API_KEY')

model = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=20,
    max_retries=0,
)


template1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables=['topic']
)
template2 = PromptTemplate(
    template = 'write a 5 line summary on the following text. /n {text}',
    input_variables = ['text']
)

prompt1 = template1.invoke({
    'topic': 'blackhole'
})
result = model.invoke(prompt1)

prompt2 = template2.invoke({
    'text': result.content
})
result = model.invoke(prompt2)
print(result.content)