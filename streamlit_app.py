import streamlit as st
from rag import retrieve_context
from llm_chain import generate_response

st.set_page_config(
    page_title="Mental Health Chatbot",
    page_icon="🧠"
)

st.title("🧠 Chotu Mental Health Chatbot")
st.caption("A supportive, non-judgmental AI companion")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("How are you feeling today?")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            context = retrieve_context(user_input)
            response = generate_response(context, user_input)
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
