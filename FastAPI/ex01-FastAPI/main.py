from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
    # uvicorn main:app --reload