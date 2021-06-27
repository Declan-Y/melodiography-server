from fastapi.testclient import TestClient
import pytest
from .main import app
import json
from object_storage.minio_client import client as minio_client


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
    
@pytest.fixture
def create_bucket():
    yield minio_client.make_bucket("test-bucket")
    minio_client.remove_bucket("test-bucket")


def test_get_presigned_url(create_bucket):
    response = client.get("/get-presigned-url/?bucket=test-bucket")
    assert response.status_code == 200



def test_put_presigned_url(create_bucket):
    response = client.get("/put-presigned-url/?bucket=test-bucket")
    assert response.status_code == 200

