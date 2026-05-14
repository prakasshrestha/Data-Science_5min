import os
from google import genai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
st.title('Youtube Video Summarization')

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])


video = st.text_input("Enter Video Link")


def vid(video):
    video1=video[17:28]
    return video1


def getts(video):
    videoid = vid(video)
    ytt_api = YouTubeTranscriptApi()
    transcript_text=ytt_api.fetch(videoid)
        
    return transcript_text

if(st.button('Summary')):
    transcript = getts(video)
    prompt = f"""
    You are an expert linguist, who is good at summarizing the content.
    Help me summarizing the content into: 100 words.
    
    ```
    {transcript}
    ```
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,)
    st.success(response.text)