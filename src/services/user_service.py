"""사용자 조회."""

from src.models.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter_by(email=email).first()

    def find_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter_by(id=user_id).first()
