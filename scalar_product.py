# CS 103 Lab 10

# Terrance Blount

import numpy 

def scalarProd(v,w):
    
    """ A sum of 2 vectors in n-space.
    
    Params: A 2 tuple point (V)
            another 2 tuple point (W)
            
    returns: Distance of (V,W)
    
    """
    
    v = x[0] + x[1]
    w = y[0] + y[1]
    
    return np.array(v*w)

def angleV(P,Q):
    
    """ Computes angle between 2 vectors.
    Params: Helper Function between 0 and 180
    returns: distance between 2 vector
    
    """
    
    P = 0
    Q = 180
    return scalarProd[P,Q]
    
def crossP(v,w):
    
    """ Cross product of 2 vectors in 3 space
    
    Params: 3-tuple vectors
    returns: cross product of 3 tuple vectors
    
    """
    A = x[1]*y[2] - x[2]*y[1]
    B = x[0]*y[3] - x[2]*y[0]
    C = x[0]*y[1] - x[2]*y[0]
  return  (A*B*C)
    
    

    
    