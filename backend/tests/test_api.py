from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"


def test_create_and_fetch_session() -> None:
    create_response = client.post("/session/", json={"human_player_name": "Matteo"})
    assert create_response.status_code == 200
    payload = create_response.json()
    session_id = payload["session"]["session_id"]

    get_response = client.get(f"/session/{session_id}")
    assert get_response.status_code == 200
    session = get_response.json()
    assert session["session_id"] == session_id
    assert session["human_player"]["name"] == "Matteo"

    world_response = client.get(f"/world/{session_id}")
    assert world_response.status_code == 200
    world_payload = world_response.json()
    assert world_payload["session_id"] == session_id
