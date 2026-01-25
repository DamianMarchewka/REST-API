from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#=============== login tests ===============

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

# =============== users test ===============

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    users = []
    for user in response.json():
        users.append(user.get("username"))
        assert "password" not in user
    assert "admin" in users
    
# =============== register tests ===============

def test_register_success_status():
    response = client.post("/register", json={
        "username": "new_user",
        "password": "0987"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "User Created Successful"


def test_register_existing_user_conflict():
    response = client.post("/register", json={
        "username": "admin",
        "password": "6543"
    })
    data = response.json()
    assert response.status_code == 409
    assert "detail" in data or "message" in data
    assert data["detail"] == "Conflict: User already exists"

