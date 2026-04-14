import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Import any global styles here if needed
import './index.css';

const rootEl = document.getElementById('root');
if (!rootEl) {
  throw new Error('Failed to find root element');
}
const root = ReactDOM.createRoot(rootEl);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);