import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { fetchSession, Session } from '../api/api';

const SessionDetail: React.FC = () => {
  const { sessionId } = useParams<{ sessionId: string }>();
  const [session, setSession] = React.useState<Session | null>(null);
  const [error, setError] = React.useState<string | null>(null);
  const [loading, setLoading] = React.useState<boolean>(false);

  React.useEffect(() => {
    if (!sessionId) return;
    let cancelled = false;
    async function load() {
      setLoading(true);
      setError(null);
      try {
        const data = await fetchSession(sessionId);
        if (!cancelled) setSession(data);
      } catch (err) {
        if (!cancelled) setError((err as Error).message);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }
    load();
    return () => {
      cancelled = true;
    };
  }, [sessionId]);

  if (!sessionId) {
    return <p>No session id provided.</p>;
  }

  return (
    <div>
      <h1>Session Detail</h1>
      {loading && <p>Loading…</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {session && (
        <div>
          <p><strong>ID:</strong> {session.id}</p>
          <p><strong>Status:</strong> {session.status}</p>
          {session.created_at && (
            <p>
              <strong>Created At:</strong> {new Date(session.created_at).toLocaleString()}
            </p>
          )}
          <p>
            <Link to={`/world/${session.id}`}>Go to World</Link>
          </p>
          <p>
            <Link to={`/log/${session.id}`}>View Event Log</Link>
          </p>
        </div>
      )}
    </div>
  );
};

export default SessionDetail;
