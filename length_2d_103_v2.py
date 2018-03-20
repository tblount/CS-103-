# 103 Johnstone UAB Fall 2016

# Terrance Blount

# we want the point cloud in 'pts2.dat', so the autograder knows where to look
PTLIST_FILENAME = "pts2.dat"  # DO NOT CHANGE THE FILE NAME
                              # you CAN change the contents of this file to test

# helper function: read and enjoy, but do not touch
def readPts ():
    """Read a list of points in 2-space from a file.

    Normally you would pass in the filename (as a string).
    We are hardwiring the filename so that our autograder will know where to
    find it.

    DO NOT CHANGE ME.

    Returns: list of points in 2-space
    """

    pts = []
    f = open (PTLIST_FILENAME, 'r')
    for line in f:
        L = line.split()
        pts.append ((float (L[0]), float (L[1])))
    f.close()
    return pts
    
# ------------------------------------------------------------------------------

import math

def length (v):

    """ Length of a vector in 2-space.

    Params: v (2-tuple) vector in 2-space
    Returns: (float) length
    """

    # INSERT CODE HERE, replacing 'pass'
    x,y = v[0],v[1]
    return math.sqrt ((x**2) + (y**2))
    
  

def dist (P,Q):

    """ Distance in 2-space.

    Params: 
        P (2-tuple): a point in 2-space
        Q (2-tuple): another point in 2-space
    Returns: (float) dist (P,Q)
    """

    # INSERT CODE HERE, replacing 'pass'
    x = Q[0] - P[0]
    y = Q[1] - P[1]
    return length((x,y))
    

def pathLength2d (pt):

    """Length of a 2-dimensional path.

    Standard length as measured by a ruler.

    Params: pt (list of 2-tuples): path in 2-space
    Returns: (float) length of this path
    """
    
    # INSERT CODE HERE, replacing 'pass'
    path = 0
    for i in range(len(pt)-1):
        path = path + dist(pt[i],pt[i+1])
    return path
        
        
# ------------------------------------------------------------------------------
# you can test this code two ways: by changing the input file data in pts2.dat
# or directly, but more tediously, using lists of 2-tuples

print(dist((3,9),(2,9)))

print (pathLength2d ([(0,0), (1,1)]))     # answer is ~1.4142 (square root of 2)
print (pathLength2d (readPts ()))

# suggestion: run the code from the command line
# in the directory that contains the file pts2.dat, using the command
# python length_2d_103.py
# (this code might not run properly from pyzo)

