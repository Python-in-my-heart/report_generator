# Report Generator 🧾

Генератор отчетов из CSV-файлов.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

## Особенности ✨
- 📂 Чтение данных из CSV-файлов с разными названиями колонок.
- 📊 Поддержка отчетов.
- 🛠 Гибкая архитектура для добавления новых отчетов.
- ✅ Полное покрытие тестами (pytest).

---

## Установка ⚙️

1. **Клонируйте репозиторий:**
   ```sh
   git clone https://github.com/Python-in-my-heart/report_generator.git
   ```
   
   ```sh
   cd report_generator
   ```

2. **Установите зависимости.**
   ```bash
   pip install -r requirements.txt


## Использование 🚀
**Запуск отчета**
   ```sh
   python -m script.report_generator.main data1.csv data2.csv --report payout
   ```

Пример вывода:
   ```sh
   | Department | Name         | Hours | Rate |  Payout |
   |------------|--------------|-------|------|---------|
   | HR         |              |       |      |         |
   |------------|--------------|-------|------|---------|
   |            | Grace Lee    |   160 | 45.0 |  7200.0 |
   |------------|--------------|-------|------|---------|
   |            | Ivy Clark    |   158 | 38.0 |  6004.0 |
   |------------|--------------|-------|------|---------|
   |            | Liam Harris  |   155 | 42.0 |  6510.0 |
   |------------|--------------|-------|------|---------|
   |            |              |   473 |      | 19714.0 |
   |------------|--------------|-------|------|---------|
   ... (полная таблица)
   ```

## Пример данных 📝
Формат CSV:
   ```sh
   id,email,name,department,hours_worked,hourly_rate
   1,alice@example.com,Alice Johnson,Marketing,160,50
   2,bob@example.com,Bob Smith,Design,150,40
   ```
