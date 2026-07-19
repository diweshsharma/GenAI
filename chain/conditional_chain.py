from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch , RunnableLambda

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
open_key = os.getenv('OPENROUTER_API_KEY')


model = init_chat_model(model = "llama-3.3-70b-versatile" ,model_provider ="groq")
# model_2 = init_chat_model("openrouter/free", model_provider="openai",
# base_url="https://openrouter.ai/api/v1",
# api_key= open_key)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = """you a customer excutive responsible for analyzing the sentiments from the feedback that user gives \n {feedback}
    you have to classify the sentiment of the feedback is of positive or negetive type , give one word answer only which is the sentiment type and if the feedback comes in any of the sentiment type give None""",
    input_variable = ['feedback']
)

classify_chain = prompt1 | model | parser

# print(classify_chain.invoke({'feedback': 'This is a worst phone'}))

""" As I have written a good prompt it only gives positive or negative during classification but to like make the answer more stable you can use pydantic schema and use pydanticOutput Parsers"""

prompt2 = PromptTemplate(
    template = """Write an appropiate response to this positive feedback \n {feedback}""",
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = """Write an appropiate response to this negative feedback \n {feedback}""",
    input_variables = ['feedback']
)
branch_chain = RunnableBranch(
   # (condition1, chain1) syntax to write the branch it is the if condition
   #(condition2, chain2) it is the else if condition
   #default chain (it is the else condition)
   
   (lambda x:x['sentiment'] == 'positive' ,prompt2 | model | parser),
   (lambda x:x['sentiment'] == 'negative' ,prompt3 | model | parser),
   # here we have to run a chain in default chain , we don't have so we are using runnable lambda nd stating that could not find sentiment
   RunnableLambda(lambda x : "could not find sentiment")
)

chain = classify_chain | branch_chain 
response = chain.invoke({'feedback': ' this is a terrible phone'})

print(response)

