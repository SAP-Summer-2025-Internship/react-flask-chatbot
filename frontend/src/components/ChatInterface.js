// frontend/src/components/ChatInterface.js
// This component implements a chat interface for interacting with the backend API, displaying conversations between users and AI models

// Import necessary React libraries and hook functions
import React, { useState } from 'react';
// Import axios for sending HTTP requests
import axios from 'axios';
// Import component's style file
import './ChatInterface.css';

/**
 * ChatInterface component - Implements main functionality of the chat interface
 * Including message display, user input, and communication with backend API
 */
const ChatInterface = () => {
  // Use useState hook to manage conversation messages array
  // Each object in messages array contains text (message content) and sender (sender, 'user' or 'bot')
  const [messages, setMessages] = useState([]);
  
  // Manage user input box state
  const [input, setInput] = useState('');
  
  // Manage loading state, used to control UI element display and disable
  const [isLoading, setIsLoading] = useState(false);

  /**
   * Handle form submission event, send user message to backend and process response
   * @param {Event} e - Form submission event object
   */
  const handleSubmit = async (e) => {
    // Prevent default form submission behavior
    e.preventDefault();
    // If input is empty, do not perform any action
    if (!input.trim()) return;

    // Get and process user input message
    const userMessage = input.trim();
    // Clear input box
    setInput('');

    // Add user message to chat history
    const newMessages = [...messages, { text: userMessage, sender: 'user' }];
    setMessages(newMessages);

    // Set loading state to true, display loading animation
    setIsLoading(true);

    try {
      // Send POST request to backend API, passing user message
      const response = await axios.post('http://localhost:5000/api/chat', {
        message: userMessage
      });

      // Add AI's response to chat history
      setMessages([
        ...newMessages,
        { text: response.data.response, sender: 'bot' }
      ]);
    } catch (error) {
      // Handle API request errors
      console.error('Error communicating with the backend:', error);
      // Display error message in chat interface
      setMessages([
        ...newMessages,
        { text: 'Sorry, there was an error processing your request.', sender: 'bot' }
      ]);
    } finally {
      // Whether request succeeds or fails, set loading state to false
      setIsLoading(false);
    }
  };

  // Render component UI
  return (
    <div className="chat-container">
      {/* Message display area */}
      <div className="chat-messages">
        {messages.length === 0 ? (
          // Guidance text displayed when there are no messages
          <div className="empty-chat">
            <p>Ask chatbot a question to get started!</p>
          </div>
        ) : (
          // Iterate through and render all messages
          messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              <div className="message-bubble">
                {message.text}
              </div>
            </div>
          ))
        )}
        {/* Animation displayed when loading */}
        {isLoading && (
          <div className="message bot">
            <div className="message-bubble loading">
              <span>...</span>
            </div>
          </div>
        )}
      </div>
      {/* User input form */}
      <form className="chat-input-form" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)} // Update input state
          placeholder="Type your question here..."
          disabled={isLoading} // Disable input box when loading
        />
        <button 
          type="submit" 
          disabled={isLoading || !input.trim()} // Disable send button when loading or input is empty
        >
          Send
        </button>
      </form>
    </div>
  );
};

// Export ChatInterface component for use by other files
export default ChatInterface;
