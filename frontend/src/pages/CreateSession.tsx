import React from 'react';
import { useNavigate } from 'react-router-dom';
import { createSession } from '../api/api';

const CreateSession: React.FC = () => {
  const navigate = useNavigate();
  const [error, setError] = React.useState<string | null>(null);
  const [creating, setCreating] = React.useState<boolean>(false);

  const handleCreate = async () => {
    setError(null);
    setCreating(true);
    try {
      const session = await createSession();
      navigate(`/session/${session.id}`);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setCreating(false);
    }
  };

  return (
    <div>
      <h1>Create Session</h1>
      <p>This will start a new RPG session.</p>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={handleCreate} disabled={creating}>
        {creating ? 'Creating…' : 'Create'}
      </button>
    </div>
  );
};

export default CreateSession;
