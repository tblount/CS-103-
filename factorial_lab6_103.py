# 103 Johnstone UAB Fall 2016

def factorial (n):
    """Factorial, computed recursively.

    What is the base case?
    How can you express n! recursively, in terms of itself?

    Params: n (int): n >= 1
    Returns: n!
    """
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

    return n

print (factorial(5)) # should be 120
