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
    # refactored version (iterative version)
    if (n == 0): 
        return 0
    if (n == 1): 
        return 1
    else : 
        a = 1
        b = 1
        for i in range(2,n) : 
            c = a + b
            a = b 
            b = c
        return c


@app.cell
def _():
    # Tests to pass

    assert(Fibonacci(0) == 0)
    assert(Fibonacci(1) == 1)
    assert(Fibonacci(3) == 2)
    assert(Fibonacci(10) == 55)



    return


if __name__ == "__main__":
    app.run()
