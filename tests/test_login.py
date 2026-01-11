from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_successful():
    response = client.post("/login", json={
        "username": "admin",
        "password": "1234"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "admin"
    assert response.json()["message"] == "login successful"


def test_invalid_password():
    response = client.post("/login", json={
        "username": "admin",
         "password": "admin"
    })
    assert response.status_code == 401
    assert response.json() == {"detail": "invalid credentials"}


def test_invalid_user():
    response = client.post("/login", json={
        "username": "xyz",
        "password": "1234"
    })
    assert response.status_code == 401
    assert response.json() == {"detail": "invalid credentials"}