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