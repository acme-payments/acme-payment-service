"""결제 처리."""

import time

import httpx

from src.config import PG_ENDPOINT, TIMEOUT_SECONDS
from src.models.order import Order


def process_payment(order_id: int, amount: int, idempotency_key: str, retry: int = 3) -> dict:
    """PG사에 결제를 요청한다.

    타임아웃이 나도 실제로는 승인된 경우가 있어 멱등키를 함께 보낸다.
    멱등키 없이 재시도하면 중복 결제가 발생한다.
    """
    last_error = None

    for attempt in range(retry):
        try:
            response = httpx.post(
                PG_ENDPOINT,
                json={"order_id": order_id, "amount": amount},
                headers={"Idempotency-Key": idempotency_key},
                timeout=TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException as exc:
            last_error = exc
            time.sleep(2**attempt)

    raise last_error


def refund_payment(order: Order) -> dict:
    response = httpx.post(f"{PG_ENDPOINT}/{order.id}/refund", timeout=TIMEOUT_SECONDS)
    return response.json()
