import React, { PropsWithChildren } from 'react';
import { Link } from 'react-router-dom';

const Layout: React.FC<PropsWithChildren> = ({ children }) => {
  return (
    <div className="app-container" style={{ fontFamily: 'sans-serif' }}>
      <header style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
        <nav style={{ display: 'flex', gap: '1rem' }}>
          <Link to="/">Home</Link>
          <Link to="/session/create">Create Session</Link>
        </nav>
      </header>
      <main style={{ padding: '1rem' }}>{children}</main>
    </div>
  );
};

export default Layout;
