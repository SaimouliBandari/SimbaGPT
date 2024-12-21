import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.callbacks import StreamlitCallbackHandler


llm = Ollama(model="llama3.1")

st.title('Dog GPT')
st.header('Hi this is Simba.. :dog:')
st.subheader('How may i help you?')
# prompt = st.text_input(label="simba",value="", key="prompt", placeholder="ask simba", label_visibility="hidden")
# file = st.file_uploader("🧷", label_visibility="hidden")
# response = ""
# if prompt:
#     response = llm.predict(prompt)
# st.markdown(response)


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)



    search = DuckDuckGoSearchResults(name="Search")
    with st.chat_message("assistant"):
        # st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        # response = llm.predict(st.session_state.messages)
        # prompt = st.text_input(label="simba",value="", key="prompt", placeholder="ask simba", label_visibility="hidden")
        print(st.session_state.messages)
        # response = llm.predict(st.session_state.messages)
        response = ""
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)