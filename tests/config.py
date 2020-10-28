from os import getenv


class TestConfig:
    endpoint_url: str = getenv("ENDPOINT_URL")
    region_name: str = getenv("AWS_DEFAULT_REGION") or getenv("REGION_NAME")
