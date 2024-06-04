# Standard Library
import os

AWS_REGION = os.getenv("AWS_REGION", default="ap-northeast-1")
STAGE: str = os.getenv("STAGE", "dev")

API_VERSION_HASH = os.getenv("API_VERSION_HASH", default="latest")

API_CORS_ALLOWED_ORIGINS: str = os.getenv("API_CORS_ALLOWED_ORIGINS", default="http://localhost:3000")
API_CORS_ALLOWED_ORIGIN_LIST: list[str] = API_CORS_ALLOWED_ORIGINS.split(",")
