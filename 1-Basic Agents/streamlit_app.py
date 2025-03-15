import streamlit as st
from agent_memory import agent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Set page config
st.set_page_config(
    page_title="Thai Cuisine Expert",
    page_icon="🍜",
    layout="wide"
)

# Title and description
st.title("🍜 Thai Cuisine Expert")
st.markdown("""
Welcome to the Thai Cuisine Expert! I can help you with:
- Thai recipes and cooking instructions
- History of Thai cuisine
- Ingredients and techniques
- General questions about Thai food
""")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about Thai cuisine!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        response = agent.get_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This Thai Cuisine Expert is powered by:
    - GPT-4 for natural language understanding
    - A knowledge base of Thai recipes
    - Web search capabilities for additional information
    """)
    
    st.header("Sample Questions")
    st.markdown("""
    Try asking:
    - How do I make Pad Thai?
    - What is the history of Thai curry?
    - What are common Thai ingredients?
    - How do I make Tom Yum soup?
    """) 