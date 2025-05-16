from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi import Query
import bcrypt 
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

class User(BaseModel):
    name: str
    email: str
    password: str 

@app.get("/{_id}")
def read_root(_id: int):
    return {"_id" : _id}  # http://localhost:8000/42


@app.get("/items/{item_id}")
def read_item(item_id: int = None, 
              r: Union[str, None] = None):
    return {"item_id" : item_id, 
            "r"       : r}  # http://localhost:8000/items/42?r=hello


@app.post("/post/{item_id}")
def create_item(item_id: int = 0, 
                q: str | None = Query(None), 
                item: Item = None):
    return {"received_item" : item, 
            "item_id"       : item_id, 
            "q"             : q} # recive from body http://localhost:8000/post/1?q=pencil


@app.post("/user")
def create_user(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user.password = hashed_password
    return {"status"          : 200, 
            "message"         : "User created successfully", 
            "received_user"   : user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
