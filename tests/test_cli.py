# tests/test_cli.py
import pytest

from fibonacci_kata.cli import build_parser, main
from fibonacci_kata.core import fibonacci


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["15"])
    assert args.n == 15


def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "1", "--end", "5"])
    assert args.start == 1
    assert args.end == 5


def test_main_prints_single_value(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "15"])
    main()
    assert capsys.readouterr().out.strip() == str(fibonacci(15))


def test_main_prints_range(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "--start", "1", "--end", "5"])
    main()
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == [str(fibonacci(n)) for n in range(1, 6)]


def test_main_requires_an_argument(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata"])
    with pytest.raises(SystemExit):
        main()


def test_main_rejects_start_without_end(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "--start", "1"])
    with pytest.raises(SystemExit):
        main()