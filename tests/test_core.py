import pytest
from fibonacci_kata.core import Fibonacci


def _():
    # Tests to pass

    assert(Fibonacci(0) == 0)
    assert(Fibonacci(1) == 1)
    assert(Fibonacci(3) == 2)
    assert(Fibonacci(10) == 55)

    # Additional tests for large value of n
    assert(Fibonacci(100)==354224848179261915075)
    print(Fibonacci(1000))  # Result should be equal to 4.3467 × 10²⁰⁸
    assert(len(str(Fibonacci(1000)))-1 == 208)
    print(str(Fibonacci(1000))[:6]) # Result = 434665
    # the two last unit tests show that we Fibonacci(1000) = 4.3467 × 10²⁰⁸
    return