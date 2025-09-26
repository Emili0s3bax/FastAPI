from fastapi import FastAPI
from sqlmodel import SQLModel

class User(SQLModel):
    id: int
    username: str
    password: str

class UserLogin(SQLModel):
    username: str
    password: str

app = FastAPI()

users_db = {
    "admin": User(username="admin", password="1234")
}

@app.post("/login")
def login(user: UserLogin):
    for login_user in users_db:
        if user.username == login_user and user.password == users_db:
            return {"message": "Login successful"}