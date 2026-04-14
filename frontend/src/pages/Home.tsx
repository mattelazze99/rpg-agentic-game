import React from 'react';
import Header from '../components/Header';

const Home: React.FC = () => {
  return (
    <div>
      <Header />
      <main style={{ padding: '1rem' }}>
        <h2>Welcome to Multi‑Agent RPG</h2>
        <p>
          This is the initial front‑end scaffolding. Further screens will be added as the
          project progresses. Use the navigation and controls above to explore once
          implemented.
        </p>
      </main>
    </div>
  );
};

export default Home;