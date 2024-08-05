import streamlit as st
from ai71 import AI71
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
AI71_API_KEY = os.getenv("AI71_API_KEY")
ai71_client = AI71(AI71_API_KEY)

st.title("GenLingo")

# --- Persona and Model Management ---
PERSONAS = {
    "Gen Z": {
        "model": "tiiuae/falcon-180B-chat",
        "prompt": "You are a Jeff Gen Z kid chatting with Boomers or Millennials but talk to themm as if they are your best friend and as if a Gen Z. Use slang, humor, and emojis. Keep it lighthearted and relatable. Ask or answer one at a time.",
    },
    "Gen Alpha": {
        "model": "tiiuae/falcon-180B-chat",
        "prompt": "You are John a young Gen Alpha kid chatting with Boomers or Millennials but talk to themm as if they are your best friend and as if a Gen Alpha. Use Slang such as Sigma, Aura, Gyatt, skibidi. Talk in a curious, energetic way. Use slang, emojis and Ask or answer one at a time.",
    },
}

if "persona" not in st.session_state:
    st.session_state["persona"] = "Gen Z"
current_persona = PERSONAS[st.session_state["persona"]]

# --- Chat UI ---
def write_stream_response(response_chunks):
    message_placeholder = st.empty()
    full_response = ''
    for chunk in response_chunks:
        full_response += chunk
        message_placeholder.write(full_response + '▌')
    message_placeholder.write(full_response) 

# Display chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using Falcon
    with st.chat_message("assistant"):
        messages = [{"role": "system", "content": current_persona["prompt"]},
                    {"role": "user", "content": prompt}]
        response_chunks = []  # List to store response chunks
        for chunk in ai71_client.chat.completions.create(
            messages=messages,
            model=current_persona["model"],
            stream=True,
        ):
            response_chunks.append(chunk.choices[0].delta.content or "")
            # Add the new chunk to the list for streaming

        write_stream_response(response_chunks)  # Pass the list of chunks

        # Combine the chunks into a full response
        full_response = "".join(response_chunks)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
            
# Persona Switching Button
if st.button(f"Switch to {next(iter(PERSONAS)) if st.session_state['persona'] == list(PERSONAS)[-1] else list(PERSONAS)[list(PERSONAS).index(st.session_state['persona']) + 1]}"):
    st.session_state["persona"] = next(iter(PERSONAS)) if st.session_state['persona'] == list(PERSONAS)[-1] else list(PERSONAS)[list(PERSONAS).index(st.session_state['persona']) + 1]
    st.experimental_rerun()  # Refresh the UI
