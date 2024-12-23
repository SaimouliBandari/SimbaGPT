from app.chat import chat_ui
import streamlit as st

st.set_page_config(
    page_icon="avatars/simba.jpg",
    page_title="Simba Gpt",
)

chat_ui()
