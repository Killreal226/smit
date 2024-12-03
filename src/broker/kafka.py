from aiokafka import AIOKafkaProducer

import json
from datetime import datetime

from src.config import kafka_config

DATE_TIME_PATTERN = "%Y-%m-%d %H:%M:%S"


class Kafka:
    def __init__(self):
        self._producer = AIOKafkaProducer(
            bootstrap_servers=kafka_config.kafka_broker_url
        )
        self._topic = kafka_config.kafka_topic

    async def log_to_kafka(self, action: str):
        await self._producer.start()
        try:
            log_message = {
                "action": action, 
                "timestamp": datetime.now().strftime(DATE_TIME_PATTERN)
            }
            await self._producer.send_and_wait(
                self._topic, json.dumps(log_message).encode()
            )
        finally:
            await self._producer.stop()


async def get_broker() -> Kafka:
    return Kafka()