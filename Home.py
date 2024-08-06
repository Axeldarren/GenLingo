import streamlit as st
from PIL import Image


# Set the page config
logo = Image.open('./assets/logo-only-no-bg.png')
st.set_page_config(page_title="GenLingo", layout="centered", page_icon=logo)

logo_sidebar_style = """<style>
    img[data-testid="stLogo"] {
        height: 2rem !important;
    }
</style>"""

st.markdown(logo_sidebar_style, unsafe_allow_html=True)
st.logo("./assets/logo-with-inline-text-brightened.png", icon_image="./assets/logo-only-no-bg-brightened.png")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            font-family: "Poppins", sans-serif;
        }
        .feature-box {
            background-color: #243b85;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #243b85;
            margin-bottom: 20px;
            transition: 100ms ease;
        }
        .feature-box:hover {
            border-color: #eee;
        }
        .feature-title {
            font-size: 24px;
            font-weight: bold;
            color: #f5f5f5;
            margin-bottom: 10px;
        }
        .feature-description {
            font-size: 16px;
            color: #d6d6d6;
        }
        .footer {
            font-size: 14px;
            color: #6c757d;
            text-align: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

button_style = """<style>
    .stButton button {
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
    }
                           
    .stButton button:hover, .stButton button:focus {
        border-color: #3262f0 !important;
        color: #3262f0 !important;
    }

    .stButton button:active {
        color: #fff !important;
        background: #3262f0 !important;
    }
</style>"""

st.markdown(button_style, unsafe_allow_html=True)

# Hero Section
st.markdown('# Master the Language of Tomorrow with :blue[GenLingo]')
st.markdown('### :grey[Unlock the latest trends in communication and stay connected with the next generations.]')
if st.button("Try GenLingo Now!", key="gl-bot-cta1", help="Start using GenLingo"):
    st.switch_page("./pages/1_GenLingo.py")

if st.button("Search the Encyclopedia", key="ency-cta1", help="Look up the definition of a slang"):
    st.switch_page("./pages/2_Encyclopedia.py")

# About Section
st.markdown("## What is GenLingo?")
st.markdown("""
GenLingo is a smart chatbot designed to help you learn and engage with the ever-evolving slang and language styles of Gen Z and Gen Alpha. 
Perfect for parents, teachers, and anyone looking to stay connected with the latest trends.
""")
st.image("https://via.placeholder.com/600x300.png", caption="Chatbot interface showing different modes for Gen Z and Gen Alpha")

# Key Features Section
st.markdown("## Why Choose GenLingo?")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col1.markdown('<div class="feature-box"><div class="feature-title">Interactive Chatbot</div><div class="feature-description">Switch between Gen Z and Gen Alpha modes to learn their unique slang.</div></div>', unsafe_allow_html=True)
col2.markdown('<div class="feature-box"><div class="feature-title">Real-Time Updates</div><div class="feature-description">Stay updated with the latest trends and slang as they evolve.</div></div>', unsafe_allow_html=True)
col3.markdown('<div class="feature-box"><div class="feature-title">Educational Integration</div><div class="feature-description">Enhance classroom interactions by understanding students’ language.</div></div>', unsafe_allow_html=True)
col4.markdown('<div class="feature-box"><div class="feature-title">Cultural Bridge</div><div class="feature-description">Facilitate better communication between different generations.</div></div>', unsafe_allow_html=True)

# Demographics Section
st.markdown("## Understanding the Generations")
st.markdown("""
- **Gen Z (born 1997-2012):** Represents about 20% of the global population. Known for their strong presence on platforms like TikTok and Instagram, and their inclination towards social activism and mental health awareness.
- **Gen Alpha (born 2013-2025):** Expected to reach 2 billion globally by 2025. This generation is characterized by their early exposure to technology and high levels of digital proficiency.
""")

# Application Scenarios Section
st.markdown("## Who Can Benefit from GenLingo?")
st.markdown("- **For Parents:** Stay connected with your kids by understanding their language.")
st.markdown("- **For Educators:** Enhance classroom engagement by staying current with your students’ slang.")
st.markdown("- **For Marketers:** Speak the language of your audience to create more effective campaigns.")
st.markdown("- **For Mental Health Professionals:** Improve communication and understanding in therapy sessions with younger clients.")

# Cultural Bridge Section
st.markdown("## Building Bridges Across Generations")
st.markdown("""
GenLingo is not just about learning slang; it’s about fostering understanding and connection between generations. 
By bridging the communication gap, GenLingo helps reduce misunderstandings and enhances relationships in families, classrooms, and beyond.
""")

# Mental Health Support Section
st.markdown("## Supporting Mental Health Through Better Communication")
st.markdown("""
Effective communication is key to understanding and supporting the mental health of younger generations. 
By using GenLingo, you can reduce communication barriers, helping to alleviate stress and anxiety that often arise from misunderstandings.
""")

# Call-to-Action Section
st.markdown("## Ready to Connect Across Generations?")
if st.button("Try GenLingo Now!", key="gl-bot-cta2", help="Start using GenLingo"):
    st.switch_page("./pages/1_GenLingo.py")

if st.button("Search the Encyclopedia", key="ency-cta2", help="Look up the definition of a slang"):
    st.switch_page("./pages/2_Encyclopedia.py")

# Footer Section
st.markdown('<div class="footer">Developed by — Samuel T. Gunawan — Axel D. Suryanto — Jeremy T. Putra — M. Noor Abdi</div>', unsafe_allow_html=True)
