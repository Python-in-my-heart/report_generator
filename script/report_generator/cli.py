import argparse


def parse_arguments() -> argparse.Namespace:
    """Обрабатывает аргументы командной строки."""
    parser = argparse.ArgumentParser(description='Генерация отчетов на основе данных о сотрудниках.')
    parser.add_argument('files', nargs='+', help='CSV-файлы.')
    parser.add_argument('--report', required=True, help='Тип отчёта (например, payout).')
    return parser.parse_args()
