import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // We keep StrictMode to help catch bugs, but be aware it 
  // might trigger your useEffect (fetching questions) twice in dev mode.
  // This is normal React behavior!
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
