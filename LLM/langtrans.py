import os
from google import genai
import streamlit as st
st.title('Language Translation')

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

user_input = st.text_area("Enter Your Sentence")
option = st.selectbox(
     'Select Language',
     ('Hindi', 'French', 'Spanish'))

if(st.button('Translate')):
    prompt = f"""
    You are an expert linguist, who is good at translating a given sentence into target language.
    Help me translate the sentence into: {option}.
    
    ```
    {user_input}
    ```
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,)
    st.success(response.text)