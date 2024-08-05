import streamlit as st

# Set the page config
st.set_page_config(page_title="GenLingo - Speak the Language of Tomorrow", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            font-family: "Poppins", sans-serif;
        }
        a {
            text-decoration: none;
            color: #ccc !important;
        }
        .anchor {
            position: relative;
            bottom: 0.2em;
        }
        .header {
            font-size: 3em;
            font-weight: bold;
            color: #ddd;
            line-height: 1em;
            margin-bottom: 0.5em;
        }
        .subheader {
            font-size: 22px;
            color: #6c757d;
            margin-bottom: 2em;
        }
        .cta-button {
            background-color: transparent;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            text-align: center;
            border: 1px solid grey;
        }
        .cta-button:hover {
            border-color: #3262f0;
            color: #3262f0 !important;
        }
        .cta-button a {
            color: #ccc !important;
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

# Hero Section
st.markdown('<div class="header">Master the Language of Tomorrow with GenLingo</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Unlock the latest trends in communication and stay connected with the next generations.</div>', unsafe_allow_html=True)
st.markdown('<a href="#utg" class="cta-button">See How It Works</a>', unsafe_allow_html=True)

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
st.markdown('<div class="anchor" id="utg"></div>', unsafe_allow_html=True)
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
st.button("Get Started", key="get_started", help="Sign up to start using GenLingo")
st.button("Contact Us", key="contact_us", help="Get in touch with the GenLingo team")

# Footer Section
st.markdown('<div class="footer">Developed by — Samuel T. Gunawan — Axel D. Suryanto — Jeremy T. Putra — M. Noor Abdi</div>', unsafe_allow_html=True)
