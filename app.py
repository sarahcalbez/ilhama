from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model='llama3.2')

# print (llm.invoke('Tell me another  joke'))

def chat_page():
    st.header("ilhama chat", divider=True)
    # st.text(llm.invoke('Tell me another  joke'))
    
    prompt = st.chat_input("Let's talk")

    if prompt:
        with st.spinner('Loading'):
            st.write(llm.stream(prompt))

def main():
    chat_page()

if __name__ == '__main__':
    main()
