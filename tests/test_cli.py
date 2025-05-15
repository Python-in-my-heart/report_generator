from script.report_generator.cli import parse_arguments


def test_cli_arguments(monkeypatch):
    """Проверка разбора аргументов командной строки."""
    test_args = ["script.py", "data1.csv", "--report", "payout"]
    with monkeypatch.context() as m:
        m.setattr("sys.argv", test_args)
        args = parse_arguments()
        assert args.files == ["data1.csv"]
        assert args.report == "payout"
