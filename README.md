# GenLingo: Bridging the Generational Slang Gap

GenLingo is an interactive Streamlit application that empowers users to engage with and learn the dynamic slang used by Gen Z and Gen Alpha. Whether you're a parent, educator, or simply curious, GenLingo provides an insightful and fun way to stay current with evolving language trends.

## Features

- **Interactive Chatbot:** Engage in real-time conversations with "Zoey" (Gen Z) or "Max" (Gen Alpha) to practice using and understanding their unique slang.
- **Slang Encyclopedia:** A comprehensive reference for browsing and searching popular slang terms and their definitions.
- **Streamlined Interface:** User-friendly design powered by Streamlit for easy navigation and interaction.
- **AI-Powered:** Leverages the Falcon 180B language model through the ai71 library for intelligent responses and context-aware conversations.

## Tech Stack

- Frontend Framework: Streamlit
- Language Model Provider: AI71
- Language Model: Falcon 180B
- Programming Languange: Python

## Prerequisites

To run this project locally, you need to have the following software installed:
- Python 3.x
- Pip (Python package installer)
- Git (for cloning the repository)
- An AI71 API key

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://your-repository-url/genlingo.git
   cd genlingo
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API Key:**
   - Obtain an API key from the AI71 platform.
   - Create a .streamlit/secrets.toml file in your project directory.
   - Add your API key to the file:
   ```TOML
   AI71_API_KEY = "your_api_key_here"
   ```
## Usage

1. **Run the Application:**
   ```bash
   streamlit run Home.py
   ```
   This launches the GenLingo app in your browser.

## Credits
**Developers:** Samuel T. Gunawan, Axel D. Suryanto, Jeremy T. Putra, M. Noor Abdi
