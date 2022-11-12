"""HTTP 엔드포인트."""

from src.services.auth_service import AuthService


def login_view(request, user_repo):
    service = AuthService(user_repo)
    user = service.authenticate_user(request.email, request.password)
    token = service.create_access_token({"sub": str(user.id)})
    return {"access_token": token}
