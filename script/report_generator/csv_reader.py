from collections import defaultdict


def read_csv(file_path: str) -> tuple[list[str], list[list[str]]]:
    """Читает данные из CSV-файла."""
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    headers = [header.strip() for header in lines[0].split(',')]
    return headers, [line.split(',') for line in lines[1:] if line]


def normalize_field_names(headers: list[str]) -> dict[str, str]:
    """Нормализует названия колонок из CSV."""
    field_map = defaultdict(list, {
        'hourly_rate': ['hourly_rate', 'rate', 'salary'],
        'hours_worked': ['hours_worked', 'hours'],
        'name': ['name'],
        'department': ['department']
    })
    normalized = {}
    for header in headers:
        for field, aliases in field_map.items():
            if header in aliases:
                normalized[field] = header
                break
    return normalized
