from fastapi import FastAPI
from app.producer import producer_service
from app.models import Event

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await producer_service.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer_service.stop()

@app.post("/publish")
async def publish(event: Event):
    await producer_service.send("events", event.dict())
    return {"status": "message sent"}