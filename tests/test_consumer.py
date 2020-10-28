from unittest import TestCase
from urllib.parse import urlparse

from faker import Faker

from sqspy import Consumer
from .config import TestConfig


class ConsumerTest(Consumer):
    def handle_message(self, body, attributes, messages_attributes):
        return body, attributes, messages_attributes


class ConsumerTestCase(TestCase):
    def setUp(self) -> None:
        self.fake = Faker()

    def test_queue_creation(self):
        queue_name = self.fake.pystr(max_chars=10)
        consumer = ConsumerTest(
            queue_name=queue_name,
            endpoint_url=TestConfig.endpoint_url,
            region_name=TestConfig.region_name,
        )
        self.assertEqual(consumer.queue_name, queue_name)
        url = urlparse(consumer.queue.url)
        self.assertEqual(url.path, f"/100010001000/{queue_name}")

    def test_invalid_consumer(self):
        self.assertRaises(ValueError, ConsumerTest)
