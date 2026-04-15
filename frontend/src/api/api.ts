export interface Session {
  id: string;
  status: string;
  created_at?: string;
}

const API_BASE: string = import.meta.env.VITE_API_BASE ?? '';

export async function createSession(): Promise<Session> {
  const response = await fetch(`${API_BASE}/sessions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (!response.ok) {
    throw new Error('Failed to create session');
  }
  return (await response.json()) as Session;
}

export async function fetchSession(id: string): Promise<Session> {
  const response = await fetch(`${API_BASE}/sessions/${id}`);
  if (!response.ok) {
    throw new Error('Failed to fetch session');
  }
  return (await response.json()) as Session;
}

export async function healthCheck(): Promise<boolean> {
  try {
    const response = await fetch(`${API_BASE}/health`);
    return response.ok;
  } catch {
    return false;
  }
}
