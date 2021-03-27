from os import getenv
from typing import Union


class TestConfig:
    aws_access_key_id: str = "XXXXXXXXXXXXXXXX"
    aws_secret_access_key: str = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
    endpoint_url: Union[None, str] = getenv("ENDPOINT_URL")
    region_name: Union[None, str] = getenv("AWS_DEFAULT_REGION", getenv("REGION_NAME"))
