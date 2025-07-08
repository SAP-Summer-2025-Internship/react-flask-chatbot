# backend/app.py
# This file implements a Flask backend service that provides API interfaces for interacting with Ollama language models

# Import necessary libraries and modules
from flask import Flask, request, jsonify  # Flask framework core components
from flask_cors import CORS  # Used to handle Cross-Origin Resource Sharing (CORS) issues
from langchain_community.llms import Ollama  # Ollama integration in LangChain
import logging  # Python standard logging module

# Configure logging system
# Set log level to DEBUG to record detailed debugging information
logging.basicConfig(level=logging.DEBUG)
# Create a logger instance specific to the current module
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)
# Enable CORS to allow frontend pages to access this API across domains
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    API endpoint for handling chat requests
    Receives user messages and returns AI model responses
    
    HTTP Method: POST
    Request body format: JSON {"message": "user message text"}
    Return format: JSON {"response": "AI model's reply"}
    """
    # Extract JSON data from request
    data = request.json
    # Get user message, default to empty string if not provided
    user_message = data.get('message', '')

    # Validate user input
    if not user_message:
        # Return 400 error if no message is provided
        return jsonify({"error": "No message provided"}), 400

    try:
        # Log debug info: Initializing Ollama
        logger.debug(f"Initializing Ollama via LangChain")
        # Initialize Ollama client using LangChain, specify using qwen:7b model
        llm = Ollama(model="qwen:7b")

        # Log the message content sent to the model
        logger.debug(f"Sending message to model: {user_message}")
        # Call model to generate response
        response = llm.invoke(user_message)
        # Log that model response has been received
        logger.debug(f"Received response from model")

        # Return model response as JSON to client
        return jsonify({"response": response})

    except Exception as e:
        # Catch and log all possible errors
        # exc_info=True will include complete exception stack trace information
        logger.error(f"Error with LLM: {str(e)}", exc_info=True)
        # Return 500 error with error details
        return jsonify({
            "error": f"Error communicating with LLM: {str(e)}"
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check API endpoint
    Checks server status and connection status with Ollama
    
    HTTP Method: GET
    Return format: JSON containing service status information
    """
    try:
        # Try to initialize Ollama to check if connection to language model is normal
        llm = Ollama(model="qwen:7b")
        # Send a simple test query, limit returned tokens to 5
        test_response = llm.invoke("hello", max_tokens=5)
        # If successful, return JSON response with normal status
        return jsonify({
            "status": "ok",  # Service status normal
            "ollama": "connected",  # Connection to Ollama normal
            "test_response": test_response  # Contains test response content
        })
    except Exception as e:
        # If connection fails, return degraded status
        return jsonify({
            "status": "degraded",  # Service status degraded
            "ollama": "disconnected",  # Connection to Ollama failed
            "error": str(e)  # Error information
        }), 207  # Use 207 status code to indicate partial success (service running but functionality degraded)

# When running this script directly (not in import mode)
if __name__ == '__main__':
    # Start Flask application
    # debug=True: Enable debug mode, automatically restart when code changes
    # host="0.0.0.0": Listen on all network interfaces, allow external access
    # port=5000: Run service on port 5000
    app.run(debug=True, host="0.0.0.0", port=5000)
