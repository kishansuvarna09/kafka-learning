import asyncio
from aiokafka import AIOKafkaConsumer
import json

async def consume():
    consumer = AIOKafkaConsumer(
        "events",
        bootstrap_servers='localhost:9092',
        group_id="my-consumer-group",
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    await consumer.start()
    print("Kafka consumer started...")

    try:
        async for msg in consumer:
            print(f"Consumed message: {msg.value} from topic: {msg.topic}")
    
    finally:
        await consumer.stop()
        print("Kafka consumer stopped.")

if __name__ == "__main__":
    asyncio.run(consume())