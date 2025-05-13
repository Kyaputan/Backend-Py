from fastapi import FastAPI

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
    import uvicorn
    uvicorn.run("router:app", host="localhost", port=8000, reload=True)

    # uvicorn router:app --reload