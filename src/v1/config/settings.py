# Standard Library
import os

AWS_REGION = os.getenv("AWS_REGION", default="ap-northeast-1")
STAGE: str = os.getenv("STAGE", "dev")

APP_API_CORS_ALLOWED_ORIGINS: str = os.getenv("APP_API_CORS_ALLOWED_ORIGINS", default="http://localhost:3000")
APP_API_CORS_ALLOWED_ORIGIN_LIST: list[str] = APP_API_CORS_ALLOWED_ORIGINS.split(",")

APP_API_BASE_URL: str = os.getenv("APP_API_BASE_URL", default="http://localhost:3333")
