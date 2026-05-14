import os
import streamlit as st
st.title('Spam Detection')

from langchain_openai import OpenAI
model = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_area("Enter Your Message")


if(st.button('Answer')):
    prompt = f"""
    You are an expert linguist, who is good at classifying the given message into Spam/NotSpam labels.
    Help me classify Message into: Spam(Ye toh SPAM Hai!!!) and NotSpam(Ye SPAM nhi Hai).
    
    ```
    {user_input}
    ```
    """
    response = model.invoke(prompt)
    st.success(response)