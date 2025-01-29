import traceback
from langchain.schema import (
    AIMessage,
    HumanMessage,
)
from agent import agent_invoke


def run_chat_cli():
    messages = []  # Initialize an empty list to store messages
    print("Welcome to the Insait Chatbot CLI!")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "q"]:
            print("Exiting chat.")
            break

        messages.append(HumanMessage(content=user_input))

        try:
            bot_response_message = agent_invoke(messages)
            messages.append(
                AIMessage(bot_response_message)
            )  # add bot response to messages
            print("Bot:", bot_response_message)
        except Exception as e:  # Catch potential errors during agent invocation
            traceback.print_exc()
            messages.append(
                AIMessage(content="Bot: An error occurred. Please try again.")
            )  # add bot response to messages


if __name__ == "__main__":
    run_chat_cli()
