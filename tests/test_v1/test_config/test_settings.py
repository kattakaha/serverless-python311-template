# Third Party Library
from config import settings


def test_stage() -> None:
    assert isinstance(settings.STAGE, str)
    assert settings.STAGE == "dev"
    assert settings.STAGE != "prod"


def test_api_cors_allowed_origins() -> None:
    assert isinstance(settings.API_CORS_ALLOWED_ORIGINS, str)
    assert settings.API_CORS_ALLOWED_ORIGINS == "http://localhost:3000,http://localhost:3005"
    assert settings.API_CORS_ALLOWED_ORIGINS != "http://localhost:3001"
    assert settings.API_CORS_ALLOWED_ORIGINS is not None


def test_api_cors_allowed_origin_list() -> None:
    assert settings.API_CORS_ALLOWED_ORIGIN_LIST == ["http://localhost:3000", "http://localhost:3005"]
    assert "http://localhost:3000" in settings.API_CORS_ALLOWED_ORIGIN_LIST
    assert "http://localhost:3005" in settings.API_CORS_ALLOWED_ORIGIN_LIST
    assert isinstance(settings.API_CORS_ALLOWED_ORIGIN_LIST, list)
    assert settings.API_CORS_ALLOWED_ORIGIN_LIST != ["http://localhost:3001"]
    assert settings.API_CORS_ALLOWED_ORIGIN_LIST is not None
