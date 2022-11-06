"""인증 처리."""

import hashlib
import secrets
from datetime import datetime, timedelta

import jwt

from src.config import ACCESS_TOKEN_EXPIRE, SECRET_KEY, SESSION_TTL_MINUTES

_sessions: dict[str, int] = {}


def verify_password(password: str, password_hash: str) -> bool:
    return hashlib.sha256(password.encode()).hexdigest() == password_hash


def create_session(user_id: int) -> str:
    """세션을 만들고 메모리에 보관한다."""
    session_id = secrets.token_hex(16)
    _sessions[session_id] = user_id
    return session_id


def get_session_user(session_id: str) -> int | None:
    return _sessions.get(session_id)


class AuthService:
    """토큰 발급과 검증을 한곳에 모은다.

    세션 저장소에 의존하던 인증을 JWT로 옮기기 위해 서비스 계층을 분리했다.
    """

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
        to_encode["exp"] = expire
        return jwt.encode(to_encode, SECRET_KEY)

    def verify_token(self, token: str) -> dict:
        payload = jwt.decode(token, SECRET_KEY)
        return payload

    def authenticate_user(self, email: str, password: str):
        user = self.user_repo.find_by_email(email)
        if user is None or not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()
        return user


class InvalidCredentialsError(Exception):
    pass
