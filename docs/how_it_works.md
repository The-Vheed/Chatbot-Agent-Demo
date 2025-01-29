# Insait-Chatbot: Agent Documentation

## Overview
The Insait-Chatbot is a conversational agent designed for e-commerce customer support. It leverages LangChain's Agent Executor to dynamically incorporate tools that handle various user queries, such as order status retrieval, return policy information, and customer support escalation. The chatbot ensures an interactive and user-friendly experience while preventing hallucinations and unreliable responses.

## Core Functionalities
### 1. **Order Status Retrieval**
The chatbot can retrieve the status of a user’s order by utilizing the `GetOrderStatus` tool. The function determines the order status based on the first digit of the order ID.

### 2. **Return Policy Information**
The `GetAllReturnPolices` tool provides predefined return policy details, covering:
- Return period
- Returnable and non-returnable items
- Refund processing methods

### 3. **Exporting User Data**
The `ExportUserData` tool allows the chatbot to collect and store user contact details in a CSV file. This is essential for escalating cases to human representatives.

## Key Components
### 1. **Tools**
The chatbot dynamically binds tools for handling specific tasks:
- `GetOrderStatus(order_id)`: Fetches order status.
- `GetAllReturnPolices()`: Retrieves return policy details.
- `ExportUserData(full_name, email, phone)`: Validates and stores user contact information securely.

### 2. **Prompt Engineering**
The chatbot follows a structured prompt template:
- It asks one question at a time to ensure complete information is collected before responding.
- It avoids hallucinations by relying strictly on its tools.
- It maintains a friendly and easy-to-understand tone.
- It ensures policy-related queries are answered accurately using predefined policies.

### 3. **LLM & Agent Execution**
- The chatbot is powered by OpenAI's `gpt-4o` model.
- The tools are dynamically bound to the model to ensure reliable responses.
- The `AgentExecutor` handles message formatting and error parsing to ensure smooth execution.

## Execution Flow
1. **User Input Handling:**
   - The chatbot captures user input and determines which tool(s) to use.
2. **Tool Invocation:**
   - If the query requires specific information (e.g., order ID), the chatbot asks follow-up questions before proceeding.
3. **Processing & Response Generation:**
   - The chatbot calls the relevant tool(s) and formats the response accordingly.
4. **Dynamic Decision Making:**
   - The chatbot dynamically integrates multiple tools when required (e.g., checking order status and providing return policy details in a single response).

## Invocation Function
The `agent_invoke(prompt, chat_history)` function serves as the chatbot's main execution point:
- `prompt`: The user’s query.
- `chat_history`: The ongoing conversation history.
- Returns the chatbot’s processed response.

## Scalability & Flexibility
- **Dynamic Tool Addition:** New tools can be added seamlessly to support more use cases.
- **Scalable Architecture:** The chatbot can be expanded to handle complex workflows by integrating more AI models or external APIs.
- **Multi-turn Conversations:** It can manage user interactions over multiple turns without losing context.

## Conclusion
The Insait-Chatbot is a robust, scalable, and user-friendly AI assistant tailored for e-commerce applications. By dynamically leveraging tools and structuring responses effectively, it ensures high-quality customer support interactions.

