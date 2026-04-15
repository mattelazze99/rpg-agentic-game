import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import CreateSession from './pages/CreateSession';
import SessionDetail from './pages/SessionDetail';
import WorldView from './pages/WorldView';
import EventLog from './pages/EventLog';

const App: React.FC = () => {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/session/create" element={<CreateSession />} />
        <Route path="/session/:sessionId" element={<SessionDetail />} />
        <Route path="/world/:sessionId" element={<WorldView />} />
        <Route path="/log/:sessionId" element={<EventLog />} />
      </Routes>
    </Layout>
  );
};

export default App;