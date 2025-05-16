from fastapi import FastAPI
from dotenv import load_dotenv
from typing import Union
import mysql.connector
import os
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str 

load_dotenv()

mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
mysql_database = os.getenv('DB_NAME')

app = FastAPI()




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
