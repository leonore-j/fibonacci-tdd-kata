def fibonacci(n, computed = None) :
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

    # first call of the function
    if computed is None:
        computed = {0: 0, 1: 1}
    
    # refactored version (using memoization - algorith found on stackoverflow.com)
    for i in range(2, n + 1):
        if i not in computed:
            computed[i] = computed[i - 1] + computed[i - 2]
            
    return computed[n]