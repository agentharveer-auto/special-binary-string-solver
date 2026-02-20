import React, { useState } from 'react';

function App() {
  const [binaryString, setBinaryString] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Input Validation (Frontend)
    if (!/^[01]+$/.test(binaryString)) {
      setError('Invalid binary string. Please enter only 0s and 1s.');
      return;
    }

    try {
      const response = await fetch('/api/solve', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ string: binaryString }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setResult(data.result);
      setError('');
    } catch (error) {
      console.error('Error calling backend:', error);
      setError('Error communicating with the server.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Special Binary String Solver</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="binaryString">Enter Binary String:</label>
        <input
          type="text"
          id="binaryString"
          value={binaryString}
          onChange={(e) => setBinaryString(e.target.value)}
          placeholder="e.g., 101101"
        />
        <button type="submit">Solve</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {result && <p>Result: {result}</p>}
    </div>
  );
}

export default App;