"""요청 전처리."""

from src.services.auth_service import AuthService


class AuthenticationError(Exception):
    pass


def require_login(request, user_repo):
    """Authorization 헤더의 토큰을 검증하고 사용자 ID를 돌려준다."""
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        raise AuthenticationError("토큰이 필요합니다")

    service = AuthService(user_repo)
    payload = service.verify_token(header.removeprefix("Bearer "))
    return int(payload["sub"])
