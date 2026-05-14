import os
from google import genai
import streamlit as st
st.title('Question-Answers')

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

user_input = st.text_area("Enter Your Question")
if(st.button('Answer')):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_input,)
    st.success(response.text)