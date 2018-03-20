from random import*

def randList ():
    
    """Randomly sized list of random integers.

    Good for producing test data for functions with list parameters.
    
    Returns: (list of integers) random positive integers between 1 and 1000,
                                of a random size
    """

    # INSERT CODE HERE
    
    L = []
    n = randint(1,1000)
    for i in range (n):
        L.append(randint(1,1000))
    return L


def myMax (L):
    
    """Maximum.
    
    Params: L (list of integers)
    Returns: (int) max(L)
    """

    # INSERT CODE HERE
    maxint = L[0]
    
    for i in range (1,len(L)):
        if L[i] > maxint:
            maxint = L[i]
    return maxint

    
    print(myMax(randList()))


