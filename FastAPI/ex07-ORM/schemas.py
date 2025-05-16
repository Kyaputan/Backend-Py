from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(User):
    pass


class UserResponse(User):
    id: int

    class Config:
        from_attributes = True