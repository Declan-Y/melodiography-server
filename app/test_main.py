from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_generate():
    response = client.get("/generate")
    assert len(response.content) > 0
    assert response.status_code == 200


def test_save():
    response = client.post("/save")
    assert response.status_code == 200
    

