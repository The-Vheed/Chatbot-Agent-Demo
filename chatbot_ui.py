import traceback
import streamlit as st
from langchain.schema import (
    AIMessage,
    HumanMessage,
)

from agent import agent_invoke

# Set Streamlit page configuration
st.set_page_config(page_title="Insait Chatbot", page_icon=":speech_balloon:")

# App title and description
st.title("Insait Chatbot GUI")
st.markdown("Powered by OpenAI, LangChain and Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Model selection (gpt-4 or mini)
# model_choice = st.selectbox("Choose a model:", ["gpt-4o-mini", "gpt-4o"])

# Initialize ChatOpenAI model
# try:
#     chat = ChatOpenAI(temperature=0.2, model=model_choice)
# except Exception as e:
#     st.error(f"Error initializing OpenAI: {e}")
#     chat = None  # Set chat to None to prevent further errors

# Display existing messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# "walrus operator" (:=) which was introduced in Python 3.8. It's a concise way to assign a value to a variable and use that value in an expression within the same line
# User input
if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display response
    try:
        full_response = ""

        with st.chat_message("assistant"):
            # initialize the message box for the assistant
            message_placeholder = st.empty()

            messages = []

            # Loop through last 10 messages and compile them for "History"
            for msg in list(st.session_state.messages)[-10:]:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    messages.append(AIMessage(content=msg["content"]))

            prompt = messages.pop(len(messages) - 1).content

            # Stream the AI response using the compiled messages and format the output on the fly
            for response in agent_invoke(prompt, messages):
                full_response += response
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        # Add the AI's reponse to the session_state
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )

    except Exception as e:
        traceback.print_exc()
        st.error(f"Error generating response: {e}")
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Error generating response. Please check your API key and model selection.",
            }
        )
        with st.chat_message("assistant"):
            st.markdown(
                "Error generating response. Please check your API key and model selection."
            )
