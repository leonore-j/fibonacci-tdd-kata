# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fibonacci-kata==0.1.0",
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt
    from collections import Counter
    import math

    from fibonacci_kata.core import fibonacci


@app.cell
def _():
    mo.md(r"""
    # Fibonacci explorer

    Pick a range below and see how fibonacci classifies each number
    in it, both as a list and as a chart of the distribution of
    outputs. This notebook consumes the published fibonacci_kata
    package — it does not reimplement the function.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    results = [fibonacci(n,) for n in range(lo, hi + 1)]
    results
    return (results,)


@app.cell
def _(results):
    values = [int(r) for r in results]
    # Les valeurs de Fibonacci croissent de façon exponentielle : on travaille
    # en échelle logarithmique, sinon tout s'écrase dans la première barre.
    log_values = [math.log10(v) for v in values if v > 0]

    fig, ax = plt.subplots()
    ax.hist(
        log_values,
        bins=20,
        density=True,
        color="#4c72b0",
    )
    ax.set_xlabel("log10(fibonacci(n))")
    ax.set_ylabel("Density")
    ax.set_title("Distribution of Fibonacci outputs over the selected range")
    fig
    return

if __name__ == "__main__":
    app.run()
