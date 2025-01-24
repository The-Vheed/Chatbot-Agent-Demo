## Insait-Chatbot: Your E-commerce Conversational Agent

Insait-Chatbot is a user-friendly chatbot designed to handle customer support queries for your e-commerce platform. It can manage multi-turn conversations, providing accurate information on order status, return policies, and more. This versatile tool empowers you to enhance customer experience and streamline support operations.

### Getting Started

**Prerequisites:**

*   Python 3.6 or later
*   Streamlit (for GUI version)

**Installation:**

1.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Chatbot

**GUI Version:**

1.  Start the server:

    ```bash
    streamlit run chatbot_ui.py
    ```

2.  Open your web browser and navigate to `http://localhost:8501/`.

**CLI Version:**

1.  Run the script:

    ```bash
    python3 chatbot_cli.py
    ```

**Important Note:**

*   Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`. You can create a `.env` file at the root of your project with the following line: `OPENAI_API_KEY="YOUR_ACTUAL_API_KEY"`
*   Replace `YOUR_ACTUAL_API_KEY` with your actual OpenAI API key obtained from [OpenAI API](https://www.google.com/url?sa=E&source=gmail&q=https://beta.openai.com/account/api-keys).

### Using the Chatbot

The chatbot interface is intuitive and straightforward. Simply type your questions or requests, and the chatbot will respond accordingly.

**Features:**

*   **Order Status:** Get real-time updates on your order status by providing your order ID.
*   **Return Policy:** Explore the return policy details, including eligible items, timeframes, and refund processes.
*   **Human Representative:** Request to connect with a customer support representative for more complex inquiries.

**Additional Notes:**

*   The chatbot is currently for assessement purposes, and its capabilities can be improved upon request.
*   For optimal performance, ensure you have a stable internet connection.

I encourage you to explore the Insait-Chatbot and leverage its potential to enhance your customer support efforts.
