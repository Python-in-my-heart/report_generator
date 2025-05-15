from collections import defaultdict
from typing import Any


class BaseReport:
    """Базовый класс для всех отчётов."""
    @classmethod
    def generate(cls, employees: list[dict[str, Any]]) -> str:
        """Генерирует отчёт."""
        raise NotImplementedError("Метод generate должен быть реализован в подклассе.")


class PayoutReport(BaseReport):
    """Отчёт по выплатам сотрудников по отделам."""
    @classmethod
    def generate(cls, employees: list[dict[str, Any]]) -> str:
        departments = defaultdict(list)
        for emp in employees:
            departments[emp['department']].append(emp)

        # Собираем все строки для расчета ширины столбцов
        all_rows = []
        # Заголовки
        all_rows.append(("Department", "Name", "Hours", "Rate", "Payout"))

        for dept in sorted(departments):
            dept_employees = departments[dept]
            # Название отдела
            all_rows.append((dept, "", "", "", ""))
            for emp in dept_employees:
                payout = emp['hours'] * emp['rate']
                all_rows.append(("", emp['name'], str(emp['hours']), str(emp['rate']), f"{payout}"))
            # Итог по отделу
            dept_total_hours = sum(e['hours'] for e in dept_employees)
            dept_total_payout = sum(e['hours'] * e['rate'] for e in dept_employees)
            all_rows.append(("", "", str(dept_total_hours), "", f"{dept_total_payout}"))

        # Общий итог
        total_hours = sum(e['hours'] for e in employees)
        total_payout = sum(e['hours'] * e['rate'] for e in employees)
        all_rows.append(("", "", "", "", ""))
        all_rows.append(("", "", str(total_hours), "", f"{total_payout}"))

        # Определяем максимальную ширину для каждого столбца
        col_widths = [
            max(len(str(row[i])) for row in all_rows) for i in range(5)
        ]

        # Форматируем строки с выравниванием
        formatted_rows = []
        for row in all_rows:
            # Заголовок
            if row[0] == "Department":
                line = "| " + " | ".join(
                    f"{col.ljust(width)}" if i == 1 else f"{col.center(width)}"
                    for i, (col, width) in enumerate(zip(row, col_widths))
                ) + " |"
                formatted_rows.append(line)
                formatted_rows.append("|-" + "-|-".join("-" * width for width in col_widths) + "-|")
            else:
                # Данные: Name (левый), Hours/Cost (правый)
                formatted = []
                for i, (col, width) in enumerate(zip(row, col_widths)):
                    # Department и Name выравниваем по левому краю
                    if i in [0, 1]:
                        formatted.append(f"{col.ljust(width)}")
                    # Числа выравниваем по правому краю
                    else:
                        formatted.append(f"{col.rjust(width)}")
                formatted_rows.append("| " + " | ".join(formatted) + " |")
                formatted_rows.append("|-" + "-|-".join("-" * width for width in col_widths) + "-|")

        return "\n".join(formatted_rows)


class AvgRateReport(BaseReport):
    """Отчёт средней ставки по отделам."""
    @classmethod
    def generate(cls, employees: list[dict[str, Any]]) -> str:
        departments = defaultdict(list)
        for emp in employees:
            departments[emp['department']].append(emp['rate'])

        # Сбор данных для таблицы
        rows = [("Department", "Avg Rate")]
        for dept in sorted(departments):
            avg = sum(departments[dept]) / len(departments[dept])
            rows.append((dept, f"{avg:.2f}"))

        # Форматирование (аналогично payout)
        col_widths = [max(len(str(row[i])) for row in rows) for i in range(2)]
        formatted = [
            f"| {row[0].ljust(col_widths[0])} | {row[1].rjust(col_widths[1])} |"
            for row in rows
        ]
        formatted.insert(1, f"|{'-' * (col_widths[0] + 2)}|{'-' * (col_widths[1] + 2)}|")
        return "\n".join(formatted)


REPORT_REGISTRY = {
    'payout': PayoutReport,
    'avg_rate': AvgRateReport,
}
