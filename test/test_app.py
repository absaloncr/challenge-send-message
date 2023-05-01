import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_send_message_with_valid_payload_and_api_key(client):
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "some-unique-jwt"
    }
    response = client.post('/DevOps', json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json == {"message": "Hello Juan Perez your message, will be sent"}

def test_send_message_with_missing_payload_fields(client):
    payload = {}
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "some-unique-jwt"
    }
    response = client.post('/DevOps', json=payload, headers=headers)
    assert response.status_code == 400
    assert response.data == b'ERROR INCOMPLETE DATA'

def test_send_message_with_invalid_api_key(client):
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }
    headers = {"X-API-Key": "invalid-api-key"}
    response = client.post('/DevOps', json=payload, headers=headers)
    assert response.status_code == 401
    assert response.data == b'ERROR X-API-Key NOT FOUND or IS INVALID'

def test_send_message_with_jwt_not_found(client):
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
    }
    response = client.post('/DevOps', json=payload, headers=headers)
    assert response.status_code == 401
    assert response.data == b'ERROR X-JWT-KWY NOT FOUND'

def test_send_message_with_invalid_http_method(client):
    headers = {"X-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"}
    response = client.get('/DevOps', headers=headers)
    assert response.status_code == 405
    assert response.data == b'ERROR INVALID METHOD'
