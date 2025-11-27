from aiokafka import AIOKafkaProducer
import json
import asyncio

class KafkaProducerService:
    def __init__(self):
        self.producer = None

    async def start(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()

    async def send(self, topic: str, message: dict):
        if not self.producer:
            raise Exception("Producer not started. Call start() before sending messages.")
        await self.producer.send_and_wait(topic, message)

producer_service = KafkaProducerService()