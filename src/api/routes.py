"""HTTP 엔드포인트."""

from src.services.auth_service import authenticate_user, create_session


def login_view(request, user_repo):
    user = authenticate_user(user_repo, request.email, request.password)
    session_id = create_session(user.id)
    return {"session_id": session_id}
