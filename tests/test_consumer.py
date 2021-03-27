from urllib.parse import urlparse

from .base_test_case import BaseTestCase, ConsumerTest


class ConsumerTestCase(BaseTestCase):
    def test_queue_creation(self):
        queue_name = self.fake.pystr(max_chars=10)
        consumer = self.get_consumer(queue_name)
        self.assertEqual(consumer.queue_name, queue_name)
        url = urlparse(consumer.queue.url)
        self.assertEqual(url.path, f"/100010001000/{queue_name}")

    def test_invalid_consumer(self):
        self.assertRaises(ValueError, ConsumerTest)

    def test_consumer_not_allowed_to_create_queue(self):
        queue_name = self.fake.pystr(max_chars=10)
        self.assertRaises(ValueError, self.get_consumer, queue_name, create_queue=False)

    def test_consumer_has_error_queue(self):
        queue_name = self.fake.pystr(max_chars=10)
        error_queue_name = f"error-{queue_name}"
        consumer = self.get_consumer(
            queue_name=queue_name,
            error_queue=error_queue_name,
        )
        self.assertEqual(consumer.queue_name, queue_name)
