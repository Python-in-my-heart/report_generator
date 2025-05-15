import pytest

from script.report_generator.base import PayoutReport


@pytest.fixture
def sample_employees():
    return [
        {"name": "Grace Lee", "department": "HR", "hours": 160, "rate": 45.0},
        {"name": "Ivy Clark", "department": "HR", "hours": 158, "rate": 38.0},
        {"name": "Liam Harris", "department": "HR", "hours": 155, "rate": 42.0},
        {"name": "Henry Martin", "department": "Marketing", "hours": 150, "rate": 35.0},
        {"name": "Karen White", "department": "Sales", "hours": 165, "rate": 50.0},
        {"name": "Mia Young", "department": "Sales", "hours": 160, "rate": 37.0},
    ]


def test_payout_report_structure(sample_employees):
    report = PayoutReport.generate(sample_employees)
    lines = report.split("\n")
    # Проверка заголовков
    assert lines[0] == "| Department | Name         | Hours | Rate |  Payout |"
    assert "|------------|--------------|-------|------|---------|" in lines[1]
    # Проверка структуры HR отдела
    hr_section = [
        "| HR         |              |       |      |         |",
        "|            | Grace Lee    |   160 | 45.0 |  7200.0 |",
        "|            | Ivy Clark    |   158 | 38.0 |  6004.0 |",
        "|            | Liam Harris  |   155 | 42.0 |  6510.0 |",
        "|            |              |   473 |      | 19714.0 |"
    ]
    for line in hr_section:
        assert line in lines
    # Проверка структуры Marketing
    marketing_section = [
        "| Marketing  |              |       |      |         |",
        "|            | Henry Martin |   150 | 35.0 |  5250.0 |",
        "|            |              |   150 |      |  5250.0 |"
    ]
    for line in marketing_section:
        assert line in lines
    # Проверка структуры Sales
    sales_section = [
        "| Sales      |              |       |      |         |",
        "|            | Karen White  |   165 | 50.0 |  8250.0 |",
        "|            | Mia Young    |   160 | 37.0 |  5920.0 |",
        "|            |              |   325 |      | 14170.0 |"
    ]
    for line in sales_section:
        assert line in lines
    # Проверка общего итога
    assert "|            |              |   948 |      | 39134.0 |" in lines


def test_separators_consistency(sample_employees):
    report = PayoutReport.generate(sample_employees)
    separators = [line for line in report.split("\n") if line.startswith("|------------")]
    # Проверка количества разделителей (15 разделителей для 6 сотрудников + 3 отдела + итоги)
    assert len(separators) == 15


def test_numeric_formatting(sample_employees):
    report = PayoutReport.generate(sample_employees)
    # Проверка формата чисел
    assert "|   160 | 45.0 |  7200.0 |" in report
    assert "|   158 | 38.0 |  6004.0 |" in report
    assert "|   325 |      | 14170.0 |" in report
    assert "|   948 |      | 39134.0 |" in report
