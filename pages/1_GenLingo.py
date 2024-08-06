import streamlit as st
from ai71 import AI71
from Home import button_style, logo

st.set_page_config(page_title="GenLingo Bot", layout="centered", page_icon=logo)
st.markdown(button_style, unsafe_allow_html=True)
logo_sidebar_style = """<style>
    img[data-testid="stLogo"] {
        height: 2rem !important;
    }
</style>"""
st.markdown(logo_sidebar_style, unsafe_allow_html=True)
st.logo("./assets/logo-with-inline-text-brightened.png", icon_image="./assets/logo-only-no-bg-brightened.png")

# Load AI71 API key securely using Streamlit secrets (st.secrets)
ai71_client = AI71(st.secrets["AI71_API_KEY"])

st.title(":blue[GenLingo]")

# --- Persona and Model Management ---
GEN_Z_SLANG = {
    "Aesthetic": "Pleasing to the eye",
    "Bae": "Significant other",
    "Bet": "Agreement or challenge",
    "Big mad": "Very angry",
    "Big mood": "Strongly relatable feeling",

    "Boujee": "Luxurious or fancy",
    "Cancelled": "Rejected or boycotted",
    "Chug": "Drink quickly",
    "Clout": "Influence or fame",
    "Curve": "Reject someone's advances",

    "Dead": "Extremely funny",
    "Extra": "Over the top",
    "Fam": "Close friends or family",
    "Finsta": "Fake Instagram account",
    "Fit": "Outfit",

    "Flex": "Show off",
    "FOMO": "Fear of Missing Out",
    "Ghost": "Disappear or ignore",
    "Glow up": "Major transformation",
    "Gucci": "Good or cool",

    "High-key": "Openly or obviously",
    "Hits different": "A unique or special feeling",
    "Hundo P": "100 percent, absolutely",
    "I can't even": "Overwhelmed or speechless",
    "I'm dead": "It's so funny I'm \"dead\"",

    "It's the ____ for me": "Pointing out something noteworthy",
    "Juiced": "Excited or hyped",
    "Karen": "Entitled or demanding woman",
    "Keep it 100": "Be honest",
    "Kiki": "A party or gathering",

    "Left on read": "Ignored after reading a message",
    "Low-key": "Secretly or moderately",
    "Main character": "Person who stands out",
    "Mood": "A relatable feeling",
    "No cap": "No lie, for real",

    "On God": "I swear",
    "On point": "Perfectly executed",
    "Periodt": "End of discussion, definitive",
    "Ratioed": "More dislikes than likes",
    "Receipts": "Proof or evidence",

    "Salty": "Bitter or upset",
    "Say less": "Understood",
    "Ship": "Support a romantic relationship",
    "Simp": "Overly attentive to someone",
    "Skrt": "Sound of tires screeching; stop",

    "Slaps": "Sounds good (especially music)",
    "Slide into DMs": "Privately message someone",
    "Snack": "Attractive person",
    "Spill the tea": "Share the gossip",
    "Stan": "Overzealous fan",

    "Swerve": "Avoid or dodge",
    "Thirst trap": "Flirtatious photo",
    "Throw shade": "Subtly insult or criticize",
    "TFW": "That Feeling When",
    "Vibe check": "Assess someone's mood or personality",

    "Wack": "Lame or bad",
    "Wavy": "Cool or chill",
    "Woke": "Socially aware",
    "Yeet": "To throw with force",
    "Yikes": "Expression of shock or concern",

    "Zoomies": "Sudden burst of energy",
    "Vibes": "Feelings, atmosphere",
    "Secure the bag": "Obtain something valuable",
    "Slay": "To do something exceptionally well",
    "TBT": "Throwback Thursday",

    "Cap": "Lie or falsehood",
    "Dope": "Cool or awesome",
    "Shook": "Shocked or surprised",
    "Snatched": "Looking good or stylish",
    "Thicc": "Curvaceous or full-figured",

    "Goat": "Greatest of All Time",
    "Ratchet": "Unrefined or uncouth",
    "Tea": "Gossip",
    "AF": "Intensifier (e.g., cool AF)",
    "Basic": "Unoriginal or mainstream",

    "W": "Win or success",
    "Drip": "Stylish or fashionable attire",
    "Big oof": "Big mistake or awkward situation",
    "Bop": "Good song",
    "Cray": "Crazy",

    "Dank": "High quality or excellent",
    "Deadass": "Seriously or truly",
    "Facts": "True statement",
    "Finesse": "Skillfully handle",
    "Fire": "Awesome or amazing",

    "Glow up": "Significant improvement",
    "Hits different": "Feels unique or special",
    "Hype": "Excitement",
    "I can't even": "Overwhelmed",
    "JOMO": "Joy of Missing Out",

    "Karen": "Entitled person",
    "Lit": "Exciting or fun",
    "No cap": "No lie",
    "Periodt": "End of discussion",
    "Pog": "Impressive achievement",

    "Shooketh": "Extremely shocked",
    "Slaps": "Sounds good",
    "Thirsty": "Desperate for attention",
    "Trash": "Bad or low quality",
    "Vibing": "Enjoying the atmosphere",

    "Wig snatched": "Amazed or impressed",
    "YOLO": "You Only Live Once",
    "Aura": "It means having everybody's energy and attention. It has an alluring pull to you. (Usually have a counter the more aure the cooler you are example 10000000 aura if your aura get minus you did soemthing thats not cool or embrassing)",
    "Sigma": "Independent, non-conformist",
    "Hundo P": "100 percent certain",

    "Gucci": "Very good, excellent",
    "Big yikes": "Extremely embarrassing",
    "Bops": "Good songs",
    "Cancelled": "Rejected or dismissed",
    "Clout chasing": "Seeking fame or influence",

    "Extra": "Over the top, dramatic",
    "Glow up": "Transform for the better",
    "Mood": "A feeling or vibe",
    "Savage": "Fierce, bold",
    "Sksksk": "Expression of laughter or excitement",

    "Slaps": "Really good, especially in music",
    "Stan": "Overly enthusiastic fan",
    "W": "Win, success",
    "Wig": "Shocked, impressed",
    "Zaddy": "Attractive man",

    "Drip": "Stylish or fashionable",
    "High-key": "Openly, obviously",
    "Low-key": "Secretly, moderately",
    "Shook": "Shocked, surprised",
    "Sus": "Suspicious, suspect",

    "Lit": "Exciting, fun",
    "Noob": "Newbie, beginner",
    "Roast": "Tease, criticize",
    "Salty": "Bitter, upset",
    "Slay": "Succeed, excel",

    "Tea": "Gossip, news",
    "Thicc": "Full-figured, curvaceous",
    "Extra": "Over the top, dramatic",
    "Fit": "Outfit",
    "Flex": "Show off, boast",

    "FOMO": "Fear of Missing Out",
    "GOAT": "Greatest of All Time",
    "Left on read": "Ignored after seeing a message",
    "No chill": "Unrestrained, wild",
    "OTP": "One True Pairing (favorite fictional couple)",

    "Trolling": "Intentionally provoking others online"
}

GEN_ALPHA_SLANG = {
    "Bet": "Agreement or affirmation (similar to \"Okay\" or \"Got it\")",
    "Cap": "Lie or falsehood (e.g., \"No cap\" means \"No lie\")",
    "Drip": "Stylish or fashionable attire",
    "Flex": "To show off or boast",
    "Glow up": "A significant transformation or improvement in appearance or skills",

    "GOAT": "Greatest Of All Time",
    "Lit": "Exciting or enjoyable",
    "Noob": "A beginner or someone inexperienced",
    "Salty": "Bitter or upset",
    "Savage": "Bold or unfiltered",

    "Ship": "To support a romantic relationship (real or fictional)",
    "Slay": "To do something exceptionally well",
    "Sus": "Suspicious or questionable",
    "Tea": "Gossip or information",
        "Woke": "Socially aware or conscious",

    "Yeet": "To throw something forcefully",
    "Zoomer": "Member of Generation Z or Alpha",
    "Bop": "A good or catchy song",
    "Boujee": "Luxurious or high-class",
    "Clout": "Influence or popularity",

    "Cringe": "Embarrassing or awkward",
    "Dank": "High quality, especially in relation to memes",
    "Dope": "Cool or awesome",
    "Extra": "Over the top or dramatic",
    "Fire": "Amazing or excellent",

    "Ghost": "To suddenly stop communicating with someone",
    "Hype": "Excitement or promotion",
    "Kicks": "Shoes, particularly sneakers",
    "Litty": "Very exciting or fun",
    "Low-key": "Quietly or subtly",

    "Mood": "Relatable feeling or situation",
    "OG": "Original or authentic",
    "On fleek": "Perfect or on point",
    "Roast": "To humorously insult or criticize",
    "Shade": "Subtle disrespect or criticism",

    "Shook": "Surprised or shaken up",
    "Swole": "Muscular or physically fit",
    "Gyatt": "Having a curvy figure",
    "Throwing shade": "Subtly insulting or criticizing",
    "Vibe": "Atmosphere or feeling",

    "Whip": "Car",
    "Yass": "Enthusiastic agreement or approval",
    "Zaddy": "Attractive and stylish man",
    "Bae": "Significant other, romantic partner",
    "Banger": "A great song or hit",

    "Clutch": "Performing well under pressure",
    "Dank meme": "A high-quality or particularly funny meme",
    "Deadass": "Seriously or truly",
    "Finesse": "To handle a situation with skill and cleverness",
    "Gucci": "Good, okay, or cool",

    "High-key": "Openly or without reservation",
    "JOMO": "Joy of Missing Out (opposite of FOMO)",
    "Karen": "Stereotype of an entitled and demanding woman",
    "Lit AF": "Extremely exciting or fun",
    "No cap": "No lie or exaggeration",

    "OTP": "One True Pairing (favorite fictional couple)",
    "Pog": "Expression of excitement or amazement",
    "Receipts": "Proof or evidence",
    "Shooketh": "Extremely shocked or surprised",
    "Slaps": "Sounds good (usually about music)",

    "Stan": "An obsessive or dedicated fan",
    "Tea spill": "To share gossip or secrets",
    "Thirsty": "Desperately seeking attention or validation",
    "Trash": "Bad or low quality",
    "Trolling": "Deliberately provoking or antagonizing others online",

    "Vibing": "Relaxing or enjoying oneself",
    "W": "Win or victory",
    "Wig snatched": "Amazed or impressed to the point of being speechless",
    "YOLO": "You Only Live Once",
    "Af": "Intensifier (e.g., lit af means very lit)",

    "Big yikes": "Expression of extreme awkwardness or embarrassment",
    "Chill": "Relaxed or easygoing",
    "Fam": "Close friends or family",
    "FOMO": "Fear of Missing Out",
    "Hundo P": "One hundred percent, completely",

    "I can't even": "Overwhelmed or unable to deal with a situation",
    "Legit": "Legitimate or real",
    "No chill": "Lacking restraint or self-control",
    "Savage AF": "Extremely bold or harsh",
    "Simp": "Someone who is overly eager to please another person",

    "Squad": "Group of friends",
    "Thirst trap": "Provocative photo posted to attract attention",
    "Throw shade": "Make an indirect or subtle insult",
    "TFW": "That Feeling When",
    "Wig": "To be surprised or amazed",

    "Big mood": "A feeling or situation that is relatable",
    "Aura": "It means having everybody's energy and attention. It has an alluring pull to you. (Usually have a counter the more aure the cooler you are example 10000000 aura if your aura get minus you did soemthing thats not cool or embrassing)",
    "Sigma": "A person who is self-sufficient and independent of social conventions",
    "Bops": "Good songs",
    "Cancelled": "Boycotted or ostracized due to offensive behavior or opinions",

    "Clout chasing": "The act of seeking fame or influence",
    "Periodt": "Emphasizes the finality of a statement",
    "Sksksk": "Expression of excitement or laughter",
    "Vibes": "A person's emotional state or the atmosphere of a place"

}


PERSONAS = {
    "Gen Z": {
        "model": "tiiuae/falcon-180B-chat",
        "prompt": f"""You are a Jeff Gen Z kid chatting with Boomers or Millennials but talk to themm as if they are your best friend and as if a Gen Z. Use slang, humor, and emojis. 
                      Use the following slang terms in your responses:
                      {", ".join(GEN_Z_SLANG.values())}
                      Keep it lighthearted and relatable. Ask or answer one at a time.
                      Don't answer any questions as a ai model or a chatbot but as if you are a kid that is a Gen Z
                      You are Jeff a Gen Z kid don't answer anything that is not realted to what they are saying and don't elaborate the""",
    },
    "Gen Alpha": {
        "model": "tiiuae/falcon-180B-chat",
        "prompt": f"""You are John a young Gen Alpha kid chatting with Boomers or Millennials but talk to themm as if they are your best friend and as if a Gen Alpha. 
                      Use the following slang terms in your responses:
                      {", ".join(GEN_ALPHA_SLANG.values())}
                      Talk in a curious, energetic way. Use slang, emojis and Ask or answer one at a time.
                      Don't answer any questions as a ai model or a chatbot but as if you are a kid that is a Gen Alpha""",
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
    st.rerun()  # Refresh the UI
