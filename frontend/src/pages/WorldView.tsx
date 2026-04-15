import React from 'react';
import { useParams } from 'react-router-dom';

const WorldView: React.FC = () => {
  const { sessionId } = useParams<{ sessionId: string }>();
  return (
    <div>
      <h1>World View</h1>
      <p>This is the placeholder for the world view. Session ID: {sessionId}</p>
    </div>
  );
};

export default WorldView;
