# Use a Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

 # For CLI version - comment out the streamlit line and uncomment the CLI line
CMD streamlit run src/chatbot_gui.py
# CMD python3 chatbot_cli.py