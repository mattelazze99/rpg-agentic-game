/**
 * API client functions for communicating with the backend.
 *
 * These functions wrap the native `fetch` API and return typed results.  In
 * development the frontend proxies `/session` and `/world` to the backend.
 */

export interface SessionResponse {
  session_id: string;
  message: string;
}

export async function createSession(): Promise<SessionResponse> {
  const response = await fetch('/session', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({}),
  });
  if (!response.ok) {
    throw new Error('Failed to create session');
  }
  return (await response.json()) as SessionResponse;
}