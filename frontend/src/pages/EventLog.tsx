import React from 'react';
import { useParams } from 'react-router-dom';

const EventLog: React.FC = () => {
  const { sessionId } = useParams<{ sessionId: string }>();
  return (
    <div>
      <h1>Event Log</h1>
      <p>This is the placeholder for the event log. Session ID: {sessionId}</p>
    </div>
  );
};

export default EventLog;
