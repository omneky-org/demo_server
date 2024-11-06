from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def get_status():
    return {"status": "OK"}

@app.get("/hello")
async def hello_world():
    return "Hello!"
