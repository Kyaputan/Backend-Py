from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

CONNECTION_STRING = os.getenv("MONGO_URI")
client = MongoClient(CONNECTION_STRING)
db = client["shop"]

app = FastAPI()


def get_user_collection():
    return db["users"]


def transform_document(doc):
    doc["_id"] = str(doc["_id"])
    if "createdAt" in doc and isinstance(doc["createdAt"], datetime):
        doc["createdAt"] = doc["createdAt"].isoformat()
    if "updatedAt" in doc and isinstance(doc["updatedAt"], datetime):
        doc["updatedAt"] = doc["updatedAt"].isoformat()
    return doc


@app.get("/")
def read():
    return "✅ Server is running!"


@app.get("/users")
def read_users(users_collection=Depends(get_user_collection)):
    users = list(users_collection.find())
    return JSONResponse(
        content=[transform_document(user) for user in users],
        media_type="application/json",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
