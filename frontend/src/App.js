// frontend/src/App.js
import React, { useState } from 'react';
import './App.css';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>SAP Q&A App</h1>
      </header>
      <main>
        <ChatInterface />
      </main>
    </div>
  );
}

export default App;

