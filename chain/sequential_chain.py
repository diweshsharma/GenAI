from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

model = ChatGroq(model = "llama-3.3-70b-versatile")
parser = StrOutputParser()

prompt = PromptTemplate(
    template = """You are a Generalist and responsible for generating reports. you have to generate detailed report about {topic} ,
    It should be relevant to the topic and clear
    """,
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template = """Generate a 5 line summary from the following text \n {text} do not use markdowns or any special character""" ,
    input_variables = ['text']
)

chain = prompt | model | parser | prompt1 | model | parser

response = chain.invoke({'topic' : 'engineering'})
# chain.get_graph().print_ascii()
print(response)
