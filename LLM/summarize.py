import os
import streamlit as st
st.title('Summarize')

from langchain_openai import OpenAI
model = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
user_input = st.text_area("Enter Content")

if(st.button('Summary')):
    prompt = f"""
    You are an expert linguist, who is good at summarizing the content.
    Help me summarizing the content into: 2 lines.
    
    ```
    {user_input}
    ```
    """
    response = model.invoke(prompt)
    st.success(response)