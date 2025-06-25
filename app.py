import streamlit as st
from summarizer import generate_summary
from utils import display_wordcloud

st.set_page_config(page_title="GenAI Text Summarizer", page_icon="🤖")

st.title("AI Text Summarizer")
st.markdown("Summarize any document or text using a local language model.")

with st.expander("Enter//Paste your text."):
    input_text = st.text_area("Text to summarize", height=300)

if st.button("Summarize"):
    if input_text.strip() != "":
        with st.spinner("Summarizing with Gerative AI..."):
            summary = generate_summary(input_text)
            st.success("Summary generated!")
            st.markdown("✂️ Summary:")
            st.write(summary)
            st.markdown("Word Cloud of Original Text:")
            display_wordcloud(input_text)
    else:
        st.warning("Please enter some text to summarize.")