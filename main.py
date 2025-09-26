from fastapi import FastAPI
from sqlmodel import SQLModel

class UserLogin(SQLModel):
    username: str
    password: str





app = FastAPI()

users_db = {
    "Juan": "Ju@n123",
    "Ana": "An@456",
    "Luis": "Lu!s789",
    "Emilio": "Emi!io101"
}

@app.post("/login")
def login(user: UserLogin):
    for login_user in users_db:
        if user.username == login_user and user.password == users_db:
            return {"message": "Login successful"}