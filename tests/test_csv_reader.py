import pytest
from pathlib import Path

from script.report_generator.csv_reader import read_csv, normalize_field_names


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Создает временный CSV-файл для тестов."""
    content = """name,department,hours_worked,rate
Alice Johnson,Marketing,160,50"""
    file_path = tmp_path / "test.csv"
    file_path.write_text(content)
    return file_path


def test_read_csv(sample_csv: Path):
    """Проверка чтения CSV-файла."""
    headers, rows = read_csv(str(sample_csv))
    assert headers == ["name", "department", "hours_worked", "rate"]
    assert rows == [["Alice Johnson", "Marketing", "160", "50"]]


def test_normalize_fields():
    """Проверка нормализации названий полей."""
    headers = ["salary", "hours", "name", "department"]
    result = normalize_field_names(headers)
    assert result == {
        "hourly_rate": "salary",
        "hours_worked": "hours",
        "name": "name",
        "department": "department"
    }
