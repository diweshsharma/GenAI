from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os 
from langchain.core.output_parsers import StructuredOutputParser , ResponseSchema 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

schema =[
    ResponseSchema(name = 'fact-1' , description = "fact 1 about the topic")
    ResponseSchema(name = 'fact-1' , description = "fact 1 about the topic")
    ResponseSchema(name = 'fact-1' , description = "fact 1 about the topic")
]