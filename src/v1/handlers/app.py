# Standard Library
from typing import Any, List

# Third Party Library
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.openapi.models import Contact, Server
from aws_lambda_powertools.utilities.typing import LambdaContext
from config.settings import APP_API_BASE_URL, STAGE
from middlewares.common import cors_middleware, handler_middleware, log_request_response
from pydantic import BaseModel, Field
from pydantic.networks import AnyUrl
from schemas import errors

tracer = Tracer(service="ApplicationHandler")
logger = Logger(service="ApplicationHandler")

servers: List[Server] = []

# APIのサーバー情報
if STAGE == "local":
    servers.append(Server(url="http://localhost:3333", description="Local Development Server", variables=None))
elif STAGE == "dev":
    servers.append(Server(url=APP_API_BASE_URL, description="Development Server", variables=None))

app = APIGatewayRestResolver(enable_validation=True)

# ミドルウェアの登録
app.use(middlewares=[log_request_response, cors_middleware])

# Swaggerの設定
app.enable_swagger(
    path="/swagger",
    title="アプリケーションAPI仕様書",
    description="""
## 概要

アプリケーションのAPI仕様書です。

## 仕様書について

仕様書（ドキュメント）の生成は、AWS Lambda Powertools の OpenAPI version 3.1.0 仕様書を使用し、半自動で生成されています。
もし、APIについての質問や提案があれば、髙橋までご連絡ください。

## リクエストとレスポンスのフォーマット

リクエストとレスポンスのフォーマットは、JSON 形式で提供されます。
リクエストに関しての詳細は、各エンドポイントの仕様を参照してください。

""",
    contact=Contact(name="Takahashi Katsuyuki", email="kattakaha@gmail.com", url=AnyUrl("https://github.com/kkml4220")),
    servers=servers,
)


class HealthCheckSchema(BaseModel):
    status: str = Field(..., title="ステータス", description="Health Check Status", example="ok")


@app.get(
    "/healthcheck",
    cors=True,
    summary="Health Check",
    description="""
## 概要

サーバーの稼働状況を確認するためのエンドポイントです。

## 詳細

基本的には常に Status Code 200: で`ok` が返却されます。
それ以外の場合は、サーバーに問題が発生している可能性がありますのでお手数ですが、髙橋までご連絡ください。

## 変更履歴
- 2024/05/10: ヘルスチェックエンドポイントを追加
    """,
    tags=["default"],
    operation_id="healthcheck",
    response_description="Health Check Status",
    responses={
        200: {"description": "Health Check Status"},
        400: errors.BAD_REQUEST_ERROR,
        401: errors.UNAUTHORIZED_ERROR,
        500: errors.INTERNAL_SERVER_ERROR,
    },
)
def health_check() -> HealthCheckSchema:
    return HealthCheckSchema(**{"status": "ok"})


@handler_middleware
@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict, context: LambdaContext) -> Any:
    return app.resolve(event, context)
