"""인증 처리."""

import hashlib
from datetime import datetime, timedelta

import jwt

from src.config import ACCESS_TOKEN_EXPIRE, ALGORITHM, SECRET_KEY


def verify_password(password: str, password_hash: str) -> bool:
    return hashlib.sha256(password.encode()).hexdigest() == password_hash


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
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def verify_token(self, token: str, verify_exp: bool) -> dict:
        """만료 검사 여부를 선택할 수 있게 한다.

        배치에서 만료된 토큰의 사용자 정보를 읽어야 하는 경우가 있다.
        """
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_exp": verify_exp},
        )
        return payload

    def authenticate_user(self, email: str, password: str):
        user = self.user_repo.find_by_email(email)
        if user is None or not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()
        return user


class InvalidCredentialsError(Exception):
    pass
