import pytest

from script.report_generator.base import AvgRateReport


@pytest.fixture
def sample_employees() -> list[dict]:
    """Тестовые данные для отчёта по ставкам."""
    return [
        {"department": "Design", "rate": 40},
        {"department": "Design", "rate": 60},
        {"department": "Marketing", "rate": 50},
    ]


def test_avg_rate_calculation(sample_employees: list[dict]):
    """Проверка расчёта средней ставки."""
    report = AvgRateReport.generate(sample_employees)
    assert "| Design     |    50.00 |" in report
    assert "| Marketing  |    50.00 |" in report
