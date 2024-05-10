# Third Party Library
from config import settings


def test_stage() -> None:
    assert settings.STAGE == "dev"
    assert settings.STAGE != "prod"
