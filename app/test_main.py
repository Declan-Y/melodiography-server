from fastapi.testclient import TestClient

from .main import app
import json


client = TestClient(app)


def test_generate():
    response = client.get("/generate")
    assert response.status_code == 200

def test_generate_headers():
    response = client.get("/generate")
    assert 'content-disposition' in response.headers

def test_generate_content_length():
    response = client.get("/generate")
    assert len(response.content) > 0

def test_generate_content_type():
    response = client.get("/generate")
    assert response.headers['content-type'] == 'audio/midi'


def test_save():
    response = client.post(url="/save", data=json.dumps({'title': 'hello'}))
    assert response.status_code == 200
    

def test_get_presigned_url():
    response = client.get("/get-presigned-url")
    assert response.status_code == 200



def test_put_presigned_url():
    response = client.get("/put-presigned-url")
    assert response.status_code == 200

