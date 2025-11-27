from fastapi import FastAPI
from producer import producer_service

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await producer_service.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer_service.stop()

@app.post("/publish")
async def publish(message: dict):
    await producer_service.send("my_topic", message)
    return {"status": "message sent"}