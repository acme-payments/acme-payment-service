"""인증 테스트."""

import pytest

from src.api.middleware import AuthenticationError, require_login
from src.services.auth_service import AuthService


def test_토큰을_발급하고_검증한다(user_repo):
    service = AuthService(user_repo)
    token = service.create_access_token({"sub": "1"})
    payload = service.verify_token(token)
    assert payload["sub"] == "1"


def test_헤더가_없으면_거부한다(request_without_header, user_repo):
    with pytest.raises(AuthenticationError):
        require_login(request_without_header, user_repo)
