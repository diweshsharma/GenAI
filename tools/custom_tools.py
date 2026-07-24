from langchain_core.tools import tool
#1st way to make a custom tool
@tool
def multiply(a: int ,b: int) -> int:
    """multiply two numbers"""
    return a*b

# result = multiply.invoke({'a': 3, 'b': 4})
# print(result)

# #2nd way to make a custom tool
# from langchain_core.tools import StructuredTool
# from pydantic import BaseModel , Field
# class multiplytool(BaseModel):
#     a : int = Field(... , description ='first number')
#     b : int = Field(... , description ='second number')

# def multiply(a: int ,b: int) -> int:
#     """multiply two numbers"""
#     return a*b

# tool = StructuredTool.from_function(
#     func = multiply,
#     name = 'multiply',
#     args_schema = multiplytool
# )

# result = tool.invoke({'a': 3, 'b': 4})
# print(result)


#3rd way using Base tool class

# tool calling 
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
load_dotenv()

model = init_chat_model("groq:llama-3.3-70b-versatile")
# agent = create_agent(model)
agent = model.bind_tools([multiply])
query = HumanMessage('can you multiply 3 with 10')
messages = [query]
response = agent.invoke(messages)
messages.append(response)
# print(response.tool_calls)

#tool execution we have to call the tool explicitly llm just suggest the tool name and the given arrtibutes in query
execute = multiply.invoke(response.tool_calls[0])
messages.append(execute)
# print(messages)
result = agent.invoke(messages)
print(result.content)