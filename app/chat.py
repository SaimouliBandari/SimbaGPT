import streamlit as st
from .llama import get_modal

avatars = {
    "assistant": "avatars/simba.jpg",
    # "user": "https://ui-avatars.com/api/?rounded=true&name=user"
    "user": None,
}
llm = get_modal()


def chat_ui():
    st.logo("avatars/simba.jpg")
    st.title("Simba  :dog: GPT")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Hi, I'm a simba who can search the web. How can I help you?",
            }
        ]

    for msg in st.session_state.messages:
        st.chat_message(name=msg["role"], avatar=avatars[msg["role"]]).write(
            msg["content"]
        )

    if prompt := st.chat_input(placeholder="ask simba"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant", avatar=avatars["assistant"]):
            response = llm.stream(prompt)
            full_response = st.write_stream(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
