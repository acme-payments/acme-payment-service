"""서비스 설정."""

DATABASE_URL = "postgresql://localhost:5432/acme"

SECRET_KEY = "change-me-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30

PG_ENDPOINT = "https://pg.example.com/v1/payments"
TIMEOUT_SECONDS = 10
