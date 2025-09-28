import streamlit as st
import pandas as pd
from groq import Groq

# --- Load Excel data ---
FILE_PATH = 'reviews_with_sentiment.xlsx'

@st.cache_data
def load_data():
    return pd.read_excel(FILE_PATH)

df = load_data()


