import streamlit as st
from api_client import send_query

# Page config
st.set_page_config(page_title="Finance Chatbot", layout="wide")

# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Header
st.markdown("""
<div class="header">
    <h1>💰 AI Finance Assistant</h1>
    <p>Track expenses • Get insights • Smart budgeting</p>
</div>
""", unsafe_allow_html=True)

# Chat container
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input box
user_input = st.text_input("Ask anything about your finances...")

if st.button("Send"):
    if user_input:
        response = send_query(user_input)

        st.session_state.chat.append(("user", user_input))
        st.session_state.chat.append(("bot", response))

# Chat display
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)