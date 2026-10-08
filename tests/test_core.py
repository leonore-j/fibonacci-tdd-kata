import pytest

from fibonacci_kata.core import fibonacci


@pytest.mark.parametrize(
    ("n", "expected"), [(0, 0), (1, 1), (2, 1), (3, 2), (5, 5), (10, 55), (20, 6765)]
)
def test_fibonacci_small_values(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_100_exact_value():
    assert fibonacci(100) == 354224848179261915075


def test_fibonacci_1000():
    # result to long to check the exact value
    # instead we check some results properties
    # F(1000) ≈ 4.3466 × 10^208
    result = str(fibonacci(1000))
    assert len(result) == 209
    assert result.startswith("434665")


@pytest.mark.parametrize("n", [2, 10, 50, 500])
def test_fibonacci_recurrence(n):
    assert fibonacci(n) == fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.parametrize("bad_input", [1.5, "10", None])
def test_fibonacci_invalid_type_raises(bad_input):
    with pytest.raises(TypeError):
        fibonacci(bad_input)
