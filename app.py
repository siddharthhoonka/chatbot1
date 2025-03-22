import streamlit as st
import requests

# API Configuration
API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Function to get chatbot response
def chat_with_groq(message):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = '{"model": "llama3-8b-8192", "messages": [{"role": "user", "content": "' + message + '"}]}'
    
    response = requests.post(API_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    return f"Error {response.status_code}: {response.text}"

# Streamlit UI
st.title("💬 Groq Chatbot")
st.write("Ask me anything!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input field
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get response
    bot_reply = chat_with_groq(user_input)
    
    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_reply)
