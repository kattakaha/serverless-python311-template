# Third Party Library
from config import settings


def test_stage() -> None:
    assert isinstance(settings.STAGE, str)
    assert settings.STAGE == "dev"
    assert settings.STAGE != "prod"


def test_api_cors_allowed_origins() -> None:
    assert isinstance(settings.APP_API_CORS_ALLOWED_ORIGINS, str)
    assert settings.APP_API_CORS_ALLOWED_ORIGINS == "http://localhost:3000"
    assert settings.APP_API_CORS_ALLOWED_ORIGINS != "http://localhost:3001"
    assert settings.APP_API_CORS_ALLOWED_ORIGINS is not None


def test_api_cors_allowed_origin_list() -> None:
    assert settings.APP_API_CORS_ALLOWED_ORIGIN_LIST == ["http://localhost:3000"]
    assert "http://localhost:3000" in settings.APP_API_CORS_ALLOWED_ORIGIN_LIST
    assert isinstance(settings.APP_API_CORS_ALLOWED_ORIGIN_LIST, list)
    assert settings.APP_API_CORS_ALLOWED_ORIGIN_LIST != ["http://localhost:3001"]
    assert settings.APP_API_CORS_ALLOWED_ORIGIN_LIST is not None


def test_app_api_base_url() -> None:
    assert isinstance(settings.APP_API_BASE_URL, str)
    assert settings.APP_API_BASE_URL == "http://localhost:3333"
    assert settings.APP_API_BASE_URL != "http://localhost:3334"
    assert settings.APP_API_BASE_URL is not None
