import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import './App.css';


export const Header = () => {
  return (
    <header className="header">
      <h1>Transcript Analysis</h1>
      <p>Your assistant for analyzing transcripts and understanding child behavior</p>
    </header>
  );
};


export const Footer = () => {
  return (
    <footer className="footer">
      <p>&copy; Learning Seeds Inc. All rights reserved.</p>
    </footer>
  );
};



function App() {
  const [transcriptText, setTranscriptText] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    // Send the transcriptText to Flask backend
    try {
      const res = await fetch('http://127.0.0.1:5000/api/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ transcriptText }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        setError(errorData.error || 'Something went wrong');
        return;
      }

      const data = await res.json();
      setResponse(data.response);
      setError('');
    } catch (err) {
      setError('Failed to connect to the server');
    } finally {
      setIsLoading(false); // Hide loading spinner when request finishes
    }
  };

  const LLM = (
    <div className="form-container">
        <form onSubmit={handleSubmit}>
          <textarea
            value={transcriptText}
            onChange={(e) => setTranscriptText(e.target.value)}
            placeholder="Paste transcript here..."
            rows={10}
            cols={50}
          />
          <br />
          <button type="submit">Analyze</button>
        </form>
        {isLoading && <div className="loading-message">Loading...</div>}
        {error && <div className="error-message">{error}</div>}
        {response && (
          <div className="response">
            <h2>Response from Model:</h2>
            <div dangerouslySetInnerHTML={{ __html: response }} />
          </div>
        )}
      </div>
  )
  const mainContent = (
      <>
      <Header />
        {LLM}
        {console.log("hi", response)}
      <Footer />
    </>)

        
    

  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={mainContent} />
        </Routes>
    </Router>
      
    </>
  );
}

export default App;
