import os 
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


try:
    gemini_key = st.secrets["gemini_key"]
except Exception:
    gemini_key = os.getenv("gemini_key")


try:
    LANGFUSE_SECRET_KEY = st.secrets["LANGFUSE_SECRET_KEY"]
except Exception:
     LANGFUSE_SECRET_KEY= os.getenv("LANGFUSE_SECRET_KEY")


try:
    LANGFUSE_PUBLIC_KEY = st.secrets["LANGFUSE_PUBLIC_KEY"]
except Exception:
    LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")



llm=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_key
)