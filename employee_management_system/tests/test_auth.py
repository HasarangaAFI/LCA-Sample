from fastapi.testclient import TestClient
from app import create_app

app = create_app()
client = TestClient(app)

def test_register():
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login():
    response = client.post(
        "/auth/token",
        data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
