from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def render():
    return {"message": "Hello FastAPI"}

@app.get("/home")
async def Home():
    return {"message": "This is Home",
            "Family":{"Father" ,
                      "Mother",
                      "Son",
                      "Daughter"}}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
    # uvicorn router:app --reload