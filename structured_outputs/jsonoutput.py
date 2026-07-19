from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

api_key = os.getenv('OPENROUTER_API_KEY')

model = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=20,
    max_retries=0,
)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name , age and city of a fictional person  \n {format_instruction}',
    input_variables = [],
    partial_variables = {
    'format_instruction' : parser.get_format_instructions()
    }
)

prompt = template.format()

result = model.invoke(prompt)
final_res = parser.parse(result.content)
print(final_res)