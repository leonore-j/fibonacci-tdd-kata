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


if __name__ == "__main__":
    app.run()
