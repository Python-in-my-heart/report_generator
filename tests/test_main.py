import pytest

from script.report_generator.main import process_files


def test_process_files(tmp_path: pytest.TempPathFactory):
    """Проверка обработки файлов."""
    # Создаем 2 тестовых файла
    file1 = tmp_path / "file1.csv"
    file1.write_text("""name,department,hours,salary
Bob,Design,150,40""")
    file2 = tmp_path / "file2.csv"
    file2.write_text("""department,email,rate,name,hours
Design,test@example.com,60,Carol,170""")

    employees = process_files([str(file1), str(file2)])
    assert len(employees) == 2
    assert employees[0]["name"] == "Bob"
    assert employees[1]["rate"] == 60.0
