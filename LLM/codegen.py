import os
import streamlit as st
st.title('Code Generator')
from langchain_openai import OpenAI
model = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_area("Enter Problem Statement")

option = st.selectbox(
     'Select Programming Language',
     ('Python', 'C', 'C++'))

if(st.button('Generate')):
    prompt = f"""
    You are an expert coder, who is good at coding a given problem statement into target programming language.
    Help me code the problem statement into: {option}.
    
    ```
    {user_input}
    ```
    """
    response = model.invoke(prompt)
    st.success(response)