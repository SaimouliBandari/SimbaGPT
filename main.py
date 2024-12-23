from app.ui import view_init
import streamlit as st

st.con 

st.set_page_config(
    page_icon="avatars/simba.jpg",
    page_title="Simba Gpt",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


def main():
    view_init()

main()
