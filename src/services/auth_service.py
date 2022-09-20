"""인증 처리."""

import hashlib
import secrets

from src.config import SESSION_TTL_MINUTES

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


def authenticate_user(user_repo, email: str, password: str):
    user = user_repo.find_by_email(email)
    if user is None or not verify_password(password, user.password_hash):
        raise InvalidCredentialsError()
    return user


class InvalidCredentialsError(Exception):
    pass
