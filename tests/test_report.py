"""리포트 테스트."""

from src.services.report_service import build_daily_report, build_monthly_report, export_report


def test_build_daily_report가_정상_응답한다():
    result = build_daily_report({})
    assert result["status"] == "ok"

def test_build_monthly_report가_정상_응답한다():
    result = build_monthly_report(1)
    assert result["status"] == "ok"

def test_export_report가_정상_응답한다():
    result = export_report(1)
    assert result["status"] == "ok"
