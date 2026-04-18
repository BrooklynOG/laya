import streamlit as st
import os
from api_client import send_query

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Finance Chatbot", layout="wide")

# ===== LOAD CSS (FIXED) =====
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")

    if not os.path.exists(css_path):
        st.error(f"CSS file not found at: {css_path}")
        return

    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ===== HEADER =====
st.markdown("""
<div class="header">
    <h1>💰 AI Finance Assistant</h1>
    <p>Track expenses • Get insights • Smart budgeting</p>
</div>
""", unsafe_allow_html=True)

# ===== SESSION STATE =====
if "chat" not in st.session_state:
    st.session_state.chat = []

# ===== INPUT =====
user_input = st.text_input("Ask anything about your finances...")

# ===== SEND BUTTON =====
if st.button("Send"):
    if user_input:
        response = send_query(user_input)

        st.session_state.chat.append(("user", user_input))
        st.session_state.chat.append(("bot", response))

# ===== CHAT DISPLAY =====
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)
