# Insait-Chatbot: Agent Documentation

## Overview
The Insait-Chatbot is a conversational agent designed for e-commerce customer support. It leverages LangChain's Agent Executor to dynamically incorporate tools that handle various user queries, such as order status retrieval, return policy information, and customer support escalation. The chatbot ensures an interactive and user-friendly experience while preventing hallucinations and unreliable responses.

## Core Functionalities

### 1. **Order Status Retrieval**
The chatbot can retrieve the status of a user's order by utilizing the `GetOrderStatus` tool. The function determines the order status based on the first digit of the order ID.

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

## Prompt Architecture

### 1. System Prompt
The main system prompt that defines the chatbot's core behavior:

```python
"You are a very powerful conversational chatbot that asks only one question at a time until you have all the necessary data to compelete a task.\n\
You never generate fake data for any reason.\n\
Try as much as possible to make use of your available tools and rely on them to avoid hallucination or appearing dumb.\n\
Always be sure of the output of your tools.\n\
Try to sound friendly and easy to understand.\n\
You make sure to utilize the policies to answer policy-related queries"
```

This system prompt establishes five key behavioral guidelines:
1. Single question interaction pattern
2. No fake data generation
3. Tool utilization preference
4. Output verification
5. Friendly communication style
6. Policy adherence

### 2. Tool Description Prompts
Each tool includes a docstring that serves as a prompt:

#### GetOrderStatus Tool
```python
"""
Get the status of the user's order with the order_id
"""
```

#### GetAllReturnPolices Tool
```python
"""
Get all the Return Policies to help with answering related queries, e.g: Return Period, Return Method, etc
"""
```

#### ExportUserData Tool
```python
"""
Exports the user data to a CSV file to enable hand-over to a human correspondent
"""
```

### 3. Parameter Schema Prompts
The parameter schemas use Pydantic's Field descriptions as prompts:

```python
class GetOrderStatusInput(BaseModel):
    order_id: int = Field(description="The ID of the order")

class ExportUserDataInput(BaseModel):
    full_name: str = Field(description="Full name of the user")
    email: str = Field(description="Email of the user")
    phone: str = Field(description="Phone number of the user")
```

### 4. Tool Return Content as Prompts
The GetAllReturnPolices tool returns structured Q&A content that serves as a response prompt:

```python
"""
Q: What is the return policy for items purchased at our store?
A: You can return most items within 30 days of purchase for a full refund or
exchange. Items must be in their original condition, with all tags and
packaging intact. Please bring your receipt or proof of purchase when
returning items.

Q: Are there any items that cannot be returned under this policy?
A: Yes, certain items such as clearance merchandise, perishable goods, and
personal care items are non-returnable. Please check the product description
or ask a store associate for more details.

Q: How will I receive my refund?
A: Refunds will be issued to the original form of payment. If you paid by
credit card, the refund will be credited to your card. If you paid by cash or
check, you will receive a cash refund.
"""
```

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
- `prompt`: The user's query.
- `chat_history`: The ongoing conversation history.
- Returns the chatbot's processed response.

## Best Practices for Prompt Modifications

When modifying prompts, consider:

1. **System Prompt Updates**:
   - Maintain the core principles (no hallucination, tool usage, etc.)
   - Keep instructions clear and specific
   - Consider adding new guidelines for new features

2. **Tool Description Updates**:
   - Keep descriptions concise but informative
   - Include example use cases where helpful
   - Clearly state any limitations or requirements

3. **Parameter Schema Updates**:
   - Use clear, specific field descriptions
   - Include validation requirements in descriptions
   - Document any format requirements

4. **Return Content Updates**:
   - Maintain consistent formatting
   - Include all necessary information
   - Structure content for easy parsing

## Scalability & Flexibility

- **Dynamic Tool Addition:** New tools can be added seamlessly to support more use cases.
- **Scalable Architecture:** The chatbot can be expanded to handle complex workflows by integrating more AI models or external APIs.
- **Multi-turn Conversations:** It can manage user interactions over multiple turns without losing context.

## Conclusion

The Insait-Chatbot is a robust, scalable, and user-friendly AI assistant tailored for e-commerce applications. Its comprehensive prompt architecture ensures consistent behavior and reliable responses, while its modular design allows for easy expansion and maintenance. By dynamically leveraging tools and structuring responses effectively, it ensures high-quality customer support interactions.