from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_generate():
    response = client.get("/generate")
    assert response.status_code == 200