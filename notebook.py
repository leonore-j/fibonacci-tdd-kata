import marimo

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

def Fibonacci(n, computed = {0: 0, 1: 1}) :
    '''
    Reminder: the Fibonacci sequence is defined by  
    F(0) = 0  
    F(1) = 1   
    F(n) = F(n−1) + F(n−2)    for n ≥ 2
    
    '''
    # refactored version (using memoization - algorith found on stackoverflow.com)

    if n not in computed:
        computed[n] = Fibonacci(n-1, computed) + Fibonacci(n-2, computed)
    return computed[n]


@app.cell
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

    result = Fibonacci(x.value)
    mo.md(f"The {x.value}th Fibonacci number is **{result}**.")
    return


if __name__ == "__main__":
    app.run()
