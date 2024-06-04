# Standard Library
import os
from typing import List

# Third Party Library
from aws_lambda_powertools.event_handler.openapi.models import Contact, Server
from pydantic.networks import AnyUrl

# First Party Library
from v1.config.settings import STAGE

# 管理者用APIのBASE_URL
API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:3333")

# APIのAuthor情報
API_AUTHOR_NAME = "Takahashi Katsuyuki"
API_AUTHOR_EMAIL = "takahashi.k@world-wing.com"
API_AUTHOR_URL = AnyUrl("https://github.com/kkml4220")

# APIの共通のPrefix
API_COMMON_PREFIX = "v1"

# APIサーバーのAuthor情報
CONTACT = Contact(name=API_AUTHOR_NAME, email=API_AUTHOR_EMAIL, url=API_AUTHOR_URL)

# 各APIサーバーの説明
API_SERVER_DESCRIPTION = {
    "dev": "Development Server",
    "local": "Local Development Server",
}

# APIのサーバー情報
SERVERS: List[Server] = [
    Server(
        url=f"{API_BASE_URL}/{API_COMMON_PREFIX}",
        description=API_SERVER_DESCRIPTION[STAGE],
        variables=None,
    )
]
