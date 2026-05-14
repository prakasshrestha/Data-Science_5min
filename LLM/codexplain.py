import os
import streamlit as st
st.title('Code Explainer')
from langchain_openai import OpenAI
model = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_area("Enter Code")
if(st.button('Explain')):
    prompt = f"""
    You are an expert linguist, who is good at explaining the code.
    You have to act as a python code explainer.
    Your task is to help me with a step
    by step explaination of given python code snippet also generate output for the same.
    Code snippet is shared below, delimited with triple backticks
    
    ```
    {user_input}
    ```
    """
    response = model.invoke(prompt)
    st.success(response)