# Third Party Library
from aws_lambda_powertools.utilities.parser import BaseModel
from pydantic import Field
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True


class TimestampMixin(BaseModel):
    updated_at: str = Field(..., title="更新日時", description="最終更新日をISOフォーマットした文字列です", example="2021-01-01T00:00:00")  # type: ignore
    created_at: str = Field(..., title="作成日時", description="作成日をISOフォーマットした文字列です", example="2021-01-01T00:00:00")  # type: ignore
