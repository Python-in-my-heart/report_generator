from typing import Any

from .cli import parse_arguments
from .csv_reader import read_csv, normalize_field_names
from .base import REPORT_REGISTRY


def process_files(files: list[str]) -> list[dict[str, Any]]:
    """Обрабатывает CSV-файлы и возвращает данные сотрудников."""
    employees = []
    for file_path in files:
        headers, rows = read_csv(file_path)
        fields = normalize_field_names(headers)
        for row in rows:
            employee = {
                'name': row[headers.index(fields['name'])],
                'department': row[headers.index(fields['department'])],
                'hours': int(row[headers.index(fields['hours_worked'])]),
                'rate': float(row[headers.index(fields['hourly_rate'])])
            }
            employees.append(employee)
    return employees


def main():
    args = parse_arguments()
    employees = process_files(args.files)
    report = REPORT_REGISTRY[args.report].generate(employees)
    print(report)


if __name__ == "__main__":
    main()
