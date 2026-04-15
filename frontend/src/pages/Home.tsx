import React from 'react';
import { Link } from 'react-router-dom';

const Home: React.FC = () => {
  return (
    <div>
      <h1>Multi-Agent RPG</h1>
      <p>Welcome to the Multi-Agent RPG prototype.</p>
      <p>
        <Link to="/session/create">Create a new session</Link>
      </p>
    </div>
  );
};

export default Home;
