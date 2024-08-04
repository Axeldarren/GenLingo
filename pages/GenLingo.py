import streamlit as st
import google.generativeai as genai
import time

# Gemini bot
# TODO: Change to Falcon AI
# TODO: Change default icon and color scheme
st.title("GenLingo")

def write_stream_response(response):
    # for word in stream.text.split():
    #     yield f'{word} '
    #     time.sleep(0.05)
    message_placeholder = st.empty()
    full_response = ''
    for chunk in response:
            # Simulate stream of chunk
            # TODO: Chunk missing `text` if API stops mid-stream ("safety"?)
            for ch in chunk.text.split(' '):
                full_response += ch + ' '
                time.sleep(0.05)
                # Rewrites with a cursor at end
                message_placeholder.write(full_response + '▌')
    # Write full message with placeholder
    message_placeholder.write(full_response)

# set Google GenAI API key from streamlit secrets
genai.configure(api_key=st.secrets["GENAI_API_KEY"])

# set a default model
if "genai_model" not in st.session_state:
    st.session_state["genai_model"] = "gemini-1.5-flash"

model = genai.GenerativeModel(st.session_state["genai_model"])

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# accept user input
if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display bot response in chat message
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)

        write_stream_response(response)
    
    # add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
