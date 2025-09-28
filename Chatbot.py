import streamlit as st
import pandas as pd
from groq import Groq

# --- Load Excel data ---
FILE_PATH = 'reviews_with_sentiment.xlsx'

@st.cache_data
def load_data():
    return pd.read_excel(FILE_PATH)

df = load_data()

# --- Summarize insights from data ---
def get_insights(data):
    total = len(data)
    pos = len(data[data['Sentiment_Label'] == 'POSITIVE'])
    neg = len(data[data['Sentiment_Label'] == 'NEGATIVE'])
    avg_pos = data[data['Sentiment_Label'] == 'POSITIVE']['Sentiment_Score'].mean()
    avg_neg = data[data['Sentiment_Label'] == 'NEGATIVE']['Sentiment_Score'].mean()
    return f"""
    Dataset Summary:
    - Total reviews: {total}
    - Positive reviews: {pos}
    - Negative reviews: {neg}
    - Average sentiment score (positive): {avg_pos:.2f}
    - Average sentiment score (negative): {avg_neg:.2f}
    """

summary_context = get_insights(df)


