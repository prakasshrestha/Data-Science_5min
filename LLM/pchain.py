import os
import streamlit as st
st.title('Prompt Chaining')

from langchain_openai import OpenAI
model = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_area("Enter Your Statement")

if(st.button('Summary')):
    prompt1 = f"""
    You are an expert linguist, who is good at summarizing the content.
    Help me summarizing the content into: 2 lines.
    
    ```
    {user_input}
    ```
    """
    response1 = model.invoke(prompt1)
    
    prompt2 = f"""
    You need to analyse the sentiment of provided text as positive/negative.
    
    ```
    {response1}
    ```
    """
    response2 = model.invoke(prompt2)
    st.success(response1)
    st.success(response2)