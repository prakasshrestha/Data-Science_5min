import os
import streamlit as st
st.title('Sentiment Analysis')

from langchain_openai import OpenAI
model = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_area("Enter Your Review")


if(st.button('Answer')):
    prompt = f"""
    You are an expert linguist, who is good at classifying customer review sentiments into Positive/Negative labels.
    Help me classify customer reviews into: Positive(Positive Review), and Negative(Negative Review).
    
    ```
    {user_input}
    ```
    """
    response = model.invoke(prompt)
    st.success(response)