from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
import tempfile

def display_wordcloud(text):
    wc = WordCloud(width=600, height=300, background_color='white').generate(text)
    st.image(wc.to_array())

def save_uploaded_file(upload_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(upload_file.read())
        return tmp_file.name