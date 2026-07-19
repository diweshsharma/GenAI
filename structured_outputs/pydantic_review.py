from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional
import os
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

class student(BaseModel):
    name : str
    age = Optional[int] = None
    
new_student = {
    'name' : 'Diwesh'
}
std = student(**new_student)