from fastapi import FastAPI
from fastapi import HTTPException, status
from app.models import Login
from database.users_db import users_db


app = FastAPI()

@app.post("/login")
def login(data: Login):

    if data.username in users_db:
        value = users_db.get(data.username)
        if value == data.password:
            return {
                "username": data.username,
                "message": "login successful"
            }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid credentials"
    )

@app.get("/users")
def get_users():
    users = []
    for username in users_db.keys():
        users.append({"username": username})
    return users


@app.post("/register", status_code=201)
def register(data: Login):

    if data.username not in users_db:
        users_db.update({data.username: data.password})
        return {"message": "User Created Successful"}
    
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Conflict: User already exists"
    )
