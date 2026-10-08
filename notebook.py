import marimo

import pytest

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    def _():
        # Documentation 
        import marimo as mo
        return mo.md("""
        # Fibonacci

        The Fibonacci(n) function computes the nth Fibonacci number.

        - Input: n, a non-negative integer
        - Output: the nth Fibonacci number
        """)


    _()
    return


@app.function
# Fibonacci sequence 

def fibonacci(n, computed = {0: 0, 1: 1}) :
    '''
    Reminder: the Fibonacci sequence is defined by  
    F(0) = 0  
    F(1) = 1   
    F(n) = F(n−1) + F(n−2)    for n ≥ 2
    
    '''
    # raises error if the value entered is :
    if not isinstance(n, int):
        raise TypeError("n must be an integer") # not an integer
    if n < 0:
        raise ValueError("n must be non-negative") # negative
    
    # refactored version (using memoization - algorith found on stackoverflow.com)
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]


@app.cell

@pytest.mark.parametrize(("n", "expected"),
[(0, 0),(1, 1),(2, 1),(3, 2),(5, 5),(10, 55),(20, 6765)])

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


@app.cell
def _():
    # Widget to pick a value 
    import marimo as mo

    x = mo.ui.slider(start=0, stop=20,step=1)
    x
    return mo, x


@app.cell
def _(mo, x):
    # Display the result

    result = fibonacci(x.value)
    mo.md(f"The {x.value}th Fibonacci number is **{result}**.")
    return


if __name__ == "__main__":
    app.run()
