from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv('OPENROUTER_API_KEY')
import streamlit as st
from langchain_core.prompts import PromptTemplate
llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

st.header('Research Tool')

user_input = st.text_input('enter the prompt')
paper_input = st.text_input('')


if st.button('summarize'):
    result = llm.invoke(user_input)
    st.write(result.content)
    
template = PromptTemplate(template = """
                          """ , input_valriables =[])

template.invoke({
    
})