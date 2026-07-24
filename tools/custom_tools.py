from langchain_core.tools import tool
#1st way to make a custom tool
@tool
def multiply(a: int ,b: int) -> int:
    """multiply two numbers"""
    return a*b

result = multiply.invoke({'a': 3, 'b': 4})
print(result)

#2nd way to make a custom tool
from langchain_core.tools import StructuredTool
from pydantic import BaseModel , Field
class multiplytool(BaseModel):
    a : int = Field(... , description ='first number')
    b : int = Field(... , description ='second number')

def multiply(a: int ,b: int) -> int:
    """multiply two numbers"""
    return a*b

tool = StructuredTool.from_function(
    func = multiply,
    name = 'multiply',
    args_schema = multiplytool
)

result = tool.invoke({'a': 3, 'b': 4})
print(result)


#3rd way using Base tool class
