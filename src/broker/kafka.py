from aiokafka import AIOKafkaProducer

import json

from src.config import kafka_config


class Kafka:
    def __init__(self):
        self._producer = AIOKafkaProducer(
            bootstrap_servers=kafka_config.kafka_broker_url
        )
        self._topic = kafka_config.kafka_topic

    async def log_to_kafka(self):
        await self._producer.start()
        try:
            log_message = {
                "user_id": "hello"
            }
            await self._producer.send_and_wait(
                self._topic, json.dumps(log_message).encode()
            )
        finally:
            await self._producer.stop()
