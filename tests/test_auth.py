"""인증 테스트."""

from src.services.auth_service import AuthService


def test_토큰을_발급하고_검증한다(user_repo):
    service = AuthService(user_repo)
    token = service.create_access_token({"sub": "1"})
    payload = service.verify_token(token)
    assert payload["sub"] == "1"
