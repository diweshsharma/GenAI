from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

# model = ChatOpenAI(
#     model = 'openai/gpt-oss-120b:free',
#     base_url ='https://openrouter.ai/api/v1',
#     api_key = api_key
# )
model = ChatGroq(model = "llama-3.3-70b-versatile")
prompt = PromptTemplate(
    template = """You are a Generalist and responsible for generating facts. you have to generate 5 intresting facts about {topic} ,
    It should be relevant to the topic and concise
    """,
    input_variables=['topic']
    
)

parser = StrOutputParser()

chains = prompt | model | parser

result = chains.invoke({'topic' : 'black hole'})
# print(type(result))
chains.get_graph().print_ascii()