import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.function
# Fibonacci sequence 

def Fibonacci(n) :
    '''
    Reminder: the Fibonacci sequence is defined by  
    F(0) = 0  
    F(1) = 1   
    F(n) = F(n−1) + F(n−2)    for n ≥ 2
    
    '''


@app.cell
def _():
    # Tests to pass
    import random 

    assert(Fibonacci(0) == 0)
    assert(Fibonacci(1) == 1)

    n = random.randint(2,100)
    assert(Fibonacci(n) == Fibonacci(n-1) + Fibonacci(n-2))

    return


if __name__ == "__main__":
    app.run()
