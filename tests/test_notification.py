"""알림 테스트."""

from src.services.notification_service import send_notification, mark_as_read, list_notifications


def test_send_notification가_정상_응답한다():
    result = send_notification({})
    assert result["status"] == "ok"

def test_mark_as_read가_정상_응답한다():
    result = mark_as_read(1)
    assert result["status"] == "ok"

def test_list_notifications가_정상_응답한다():
    result = list_notifications(1)
    assert result["status"] == "ok"
