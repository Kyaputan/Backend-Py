from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

mork_data = [
    {"id": 1, "name": "John", "email": "John@example.com", "password": "123456"},
    {"id": 2, "name": "Jane", "email": "Jane@example.com", "password": "123456"},
    {"id": 3, "name": "Jack", "email": "Jack@example.com", "password": "123456"},
    {"id": 4, "name": "Jill", "email": "Jill@example.com", "password": "123456"},
]

class Item(BaseModel):
    name: str
    description: str

class User(BaseModel):
    id : int
    name: str
    email: str
    password: str


@app.get("/users")
def render():
    return mork_data


@app.get("/users/{user_id}")
def read_user(user_id: int):
    id = user_id - 1
    return mork_data[id]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
