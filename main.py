from fastapi import FastAPI
from sqlmodel import SQLModel


class UserLogin(SQLModel):
    username: str
    password: str

app = FastAPI()


users_db = {
    "admin": UserLogin(username="admin", password="1234")
}

@app.post("/login")
def login(user: UserLogin):
    for username, db_user in users_db.items():
        if db_user.username == user.username and db_user.password == user.password:
            return {"message": "Login successful"}
    
    return {"message": "usuario y/o contraseña incorrectos."}
