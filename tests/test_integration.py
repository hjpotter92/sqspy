from json import loads
from unittest import TestCase

from faker import Faker

from sqspy import Consumer, Producer
from .config import TestConfig


class ProducerTestCase(TestCase):
    def setUp(self) -> None:
        self.fake = Faker()

    @staticmethod
    def get_producer_consumer(queue_name: str):
        return Producer(
            queue_name=queue_name,
            endpoint_url=TestConfig.endpoint_url,
            region_name=TestConfig.region_name,
        ), Consumer(
            queue_name=queue_name,
            endpoint_url=TestConfig.endpoint_url,
            region_name=TestConfig.region_name,
            max_number_of_messages=1,
        )

    def test_message_acknowledgement(self):
        queue_name = self.fake.pystr(max_chars=10)
        producer, consumer = self.get_producer_consumer(queue_name)
        message = self.fake.json(
            data_columns={
                "name": "company",
                "phrase": "catch_phrase",
                "description": "bs",
                "address": "address",
            }
        )
        message_data = producer.publish(message)
        fetched_message = consumer.poll_messages()[0]
        self.assertEqual(fetched_message.md5_of_body, message_data.get("MD5OfMessageBody"))
        self.assertEqual(fetched_message.message_id, message_data.get("MessageId"))
        self.assertEqual(message, loads(fetched_message.body))
