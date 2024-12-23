import streamlit as st
from langchain_ollama import OllamaLLM


llm = OllamaLLM(model="llama3.1", base_url="192.168.31.96:11434")

st.title('Dog GPT')
st.header('Hi this is Simba.. :dog:')
st.subheader('How may i help you?')

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="ask simba"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response = llm.stream(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write_stream(response)