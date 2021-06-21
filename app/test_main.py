from fastapi.testclient import TestClient

from app.main import app
import json


client = TestClient(app)


def test_generate():
    response = client.get("/generate")
    assert len(response.content) > 0
    assert response.status_code == 200


def test_save():
    response = client.post(url="/save", data=json.dumps({'title': 'hello'}))
    assert response.status_code == 200
    

