import React from 'react';

const Header: React.FC = () => {
  return (
    <header
      style={{
        padding: '1rem',
        borderBottom: '1px solid #ccc',
        marginBottom: '1rem',
      }}
    >
      <h1 style={{ margin: 0 }}>Multi‑Agent RPG</h1>
    </header>
  );
};

export default Header;