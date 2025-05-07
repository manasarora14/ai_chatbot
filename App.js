import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const askQuestion = async () => {
    try {
      const res = await axios.post('http://localhost:5000/ask', { question });
      setAnswer(res.data.answer);
    } catch (err) {
      setAnswer("Error getting answer. Try again.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Legal Assistant AI</h1>
      <textarea
        rows="4"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a legal question..."
        style={{ width: '100%', padding: 10 }}
      />
      <button onClick={askQuestion} style={{ marginTop: 10 }}>Ask</button>
      <div style={{ marginTop: 20, whiteSpace: 'pre-wrap' }}>
        <strong>Answer:</strong>
        <p>{answer}</p>
      </div>
    </div>
  );
}

export default App;
