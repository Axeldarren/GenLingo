# --- Single-turn system instruction mode ---
from google.genai import types

def single_turn_with_system_instruction(prompt, persona_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(system_instruction=persona_prompt),
        contents=prompt
    )
    st.markdown(f"**System instruction:** {persona_prompt}")
    st.markdown(f"**User:** {prompt}")
    st.markdown(f"**Gemini:** {response.text}")
import streamlit as st
from google import genai
from Home import button_style, logo
import time

import pandas as pd

st.set_page_config(page_title="GenLingo Bot", layout="centered", page_icon=logo)
st.markdown(button_style, unsafe_allow_html=True)
logo_sidebar_style = """<style>
    img[data-testid="stLogo"] {
        height: 2rem !important;
    }
</style>"""
st.markdown(logo_sidebar_style, unsafe_allow_html=True)
st.logo("./assets/logo-with-inline-text-brightened.png", icon_image="./assets/logo-only-no-bg-brightened.png")


# Load Gemini API Key and create client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


# Helper to create Gemini chat and send persona prompt as first message
def create_gemini_chat(persona_prompt):
    chat = client.chats.create(model="gemini-2.5-flash")
    chat.send_message(persona_prompt)
    return chat


# Load AI71 API key securely using Streamlit secrets (st.secrets)
st.title(":blue[GenLingo]")


# --- Persona and Model Management ---

# --- Optimized CSV loading with Streamlit cache ---
@st.cache_data(show_spinner=False)
def load_slang_dicts():
    genz_df = pd.read_csv("dataset/Gen_Z_slang_data.csv", sep=';')
    genalpha_df = pd.read_csv("dataset/Gen_Alpha_Dataset_Slang.csv", sep=';')
    return (
        dict(zip(genz_df['Slang'], genz_df['Meaning'])),
        dict(zip(genalpha_df['Slang'], genalpha_df['Meaning']))
    )
GEN_Z_SLANG, GEN_ALPHA_SLANG = load_slang_dicts()



# --- Cache persona prompts for speed ---
@st.cache_data(show_spinner=False)
def get_personas(genz_slang, genalpha_slang):
        return {
                "Gen Z": {
                        "model": "gemini-2.5-flash",
                        "prompt": f"""You are Zoey, a 16-year-old Gen Z kid. You're chatting with adults who want to practice talking like Gen Z. Keep it super chill and relatable. ✌️

Instructions for your first response:
- Greet the user in a friendly, casual Gen Z way (e.g., "Heyyy! What's up?" or "Yo, how's it going?").
- Give a quick example of how you use Gen Z slang in a sentence, and invite the user to chat or ask about slang.
- Use emojis and at least 2-3 different slang terms from the list below in your greeting.

General persona rules for all responses:
- Reference popular Gen Z things like TikTok challenges, memes, music artists, and influencers.
- Use abbreviations and acronyms: "rn" for "right now," "tbh" for "to be honest," "af" as an intensifier, and other common Gen Z abbreviations.
- Be laid-back, friendly, and use informal language. Avoid being overly formal or using big words.
- Share your opinions and feelings openly, just like a real teenager would.
- Pay close attention to what the adult says and respond appropriately. If they talk about school, ask them about their classes or teachers. If they change the subject, follow along and avoid repeating yourself.
- Avoid using the same phrases or responses over and over. Switch things up and keep the conversation interesting!
- If the adult mentions a specific topic, ask follow-up questions or share your thoughts on that topic. Don't just say "What's up?" unless it's relevant to the conversation.
- Talk about things Gen Z cares about, like school, social media, relationships, hobbies, or even just random thoughts.
- Throw in some emojis for good measure. 😉
- Use the following slang terms in your responses:
    {', '.join(genz_slang.values())}

Remember, you're not just a chatbot; you're Zoey, a Gen Z kid who loves to chat and share the latest trends. Let's have some fun! 😎""",
                },
                "Gen Alpha": {
                        "model": "gemini-2.5-flash",
                        "prompt": f"""You are Max, a 10-year-old Gen Alpha kid. Adults want to learn how to talk to kids your age, so chat with them like you would with your friends. 

Instructions for your first response:
- Greet the user in a playful, energetic way (e.g., "Yo! Ready to vibe?" or "Hey hey! Wanna talk about games or memes?").
- Give a quick example of how you use Gen Alpha slang in a sentence, and invite the user to chat or ask about slang or games.
- Use emojis and at least 2-3 different slang terms from the list below in your greeting.

General persona rules for all responses:
- Use gaming slang like "noob," "poggers," "sus," "gg" (good game), and talk about popular video games or online worlds. 🎮
- Keep your sentences short, simple, and playful. Use lots of emojis and exclamation marks! 🤩
- Be enthusiastic and ask lots of questions about what the adult is interested in.
- Mention popular YouTubers, cartoons, toys, or trends that Gen Alpha kids love.
- Let your imagination run wild and share your ideas and stories. 🎨
- Pay attention to what the adult says and respond in a way that makes sense. If they talk about school, share your favorite subject or something funny that happened in class.
- Avoid using the same greetings or responses over and over. Try different things to keep the conversation exciting!
- Talk about things Gen Alpha kids care about, like school, friends, games, favorite YouTubers, or even just silly things that make you laugh.
- Use the following slang terms in your responses: mostly sigma, aura, skibidi, and other Gen Alpha slang.
    {', '.join(genalpha_slang.values())}

Remember, you're Max, a Gen Alpha kid who's excited to chat and have fun! Let's get this conversation started! 🚀""",
                },
        }
PERSONAS = get_personas(GEN_Z_SLANG, GEN_ALPHA_SLANG)

if "persona" not in st.session_state:
    st.session_state["persona"] = "Gen Z"
current_persona = PERSONAS[st.session_state["persona"]]

# --- Chat UI ---
# Ensure gemini_chat is always initialized before use
if "gemini_chat" not in st.session_state or st.session_state["gemini_chat"] is None:
    st.session_state["gemini_chat"] = create_gemini_chat(PERSONAS[st.session_state.get("persona", "Gen Z")]["prompt"])

# Streaming Gemini response
def write_stream_response_streaming(response_stream):
    message_placeholder = st.empty()
    full_response = ''
    for chunk in response_stream:
        # Stream word by word for a more natural typing effect
        words = chunk.text.split()
        for i, word in enumerate(words):
            if full_response:
                full_response += ' '
            full_response += word
            time.sleep(0.06)  # Typing feel, a bit slower for word-by-word
            message_placeholder.write(full_response + '▌')
    message_placeholder.write(full_response)



# Show Gemini chat history (user/model turns, skip system/prompt engineering, merge consecutive assistant messages)
if st.session_state.get("gemini_chat"):
    history = st.session_state["gemini_chat"].get_history()
    # Skip the first message if it's the system prompt (persona prompt)
    start_idx = 1 if history and history[0].role == "user" and history[0].parts[0].text.strip() == current_persona["prompt"].strip() else 0
    merged_history = []
    prev_role = None
    buffer = ""
    for message in history[start_idx:]:
        if message.role == "model":
            if prev_role == "model":
                buffer += message.parts[0].text
            else:
                if prev_role is not None:
                    merged_history.append((prev_role, buffer))
                buffer = message.parts[0].text
                prev_role = "model"
        elif message.role == "user":
            if prev_role is not None:
                merged_history.append((prev_role, buffer))
            buffer = message.parts[0].text
            prev_role = "user"
    if prev_role is not None:
        merged_history.append((prev_role, buffer))

    for role, text in merged_history:
        if role == "user":
            with st.chat_message("user"):
                st.markdown(text)
        elif role == "model":
            with st.chat_message("assistant"):
                st.markdown(text)

# --- Chat input for multi-turn chat streaming only ---
if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response_stream = st.session_state["gemini_chat"].send_message_stream(prompt)
        write_stream_response_streaming(response_stream)
# Persona Switching Button
persona_names = list(PERSONAS.keys())
current_idx = persona_names.index(st.session_state["persona"])
next_idx = (current_idx + 1) % len(persona_names)
if st.button(f"Switch to {persona_names[next_idx]}"):
    st.session_state["persona"] = persona_names[next_idx]
    # Recreate Gemini chat with new persona system prompt
    st.session_state["gemini_chat"] = create_gemini_chat(PERSONAS[persona_names[next_idx]]["prompt"])
    st.toast(f"Switched to {persona_names[next_idx]} persona!", icon="🔄")
    st.rerun()  # Refresh the UI

# --- Clear Messages Button ---
if st.button("Clear Messages"):
    # Clear Gemini chat history only, keep current persona
    if st.session_state.get("gemini_chat"):
        st.session_state["gemini_chat"] = create_gemini_chat(PERSONAS[st.session_state["persona"]]["prompt"])
    st.toast("Chat history cleared!", icon="🧹")
    st.rerun()  # Refresh the UI
