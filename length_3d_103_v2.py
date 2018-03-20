# 103 Johnstone UAB Fall 2016

# Terrance Blount

# we want the point cloud in 'pts3.dat', so the autograder knows where to look
PTLIST_FILENAME = "pts3.dat"  # DO NOT CHANGE THE FILE NAME
                              # you CAN change the contents of this file to test

# helper function: read and enjoy, but do not touch
def readPts ():
    """Read a list of points in 3-space from a file.

    DO NOT CHANGE ME.

    Returns: list of points in 3-space
    """

    pts = []
    f = open (PTLIST_FILENAME, 'r')
    for line in f:
        L = line.split()
        pts.append ((float (L[0]), float (L[1]), float (L[2])))
    f.close()
    return pts

# ------------------------------------------------------------------------------
    
import math

def length (v):

    """ Length of a vector in 3-space.

    Params: v (3-tuple) vector in 3-space
    Returns: (float) length
    """

    # INSERT CODE HERE, replacing 'pass'
    x,y,z = v[0],v[1],v[2]
    return math.sqrt ((x**2) + (y**2) +(z**2))

def dist (P,Q):

    """ Distance in 3-space.

    Params: 
        P (3-tuple): a point in 3-space
        Q (3-tuple): another point in 3-space
    Returns: (float) dist (P,Q)
    """

    # INSERT CODE HERE, replacing 'pass'
    x = Q[0] - P[0]
    y = Q[1] - P[1]
    z = Q[2] - P[2]
    return length((x,y,z))

def pathLength3d (pt):

    """Length of a 3-dimensional path.

    Standard length as measured by a ruler.

    Params: pt (list of 3-tuples): path in 3-space
    Returns: (float) length of this path
    """
    
    # INSERT YOUR CODE HERE, replacing 'pass'
    path = 0
    for i in range(len(pt)-1):
        path = path + dist(pt[i],pt[i+1])
    return path

# ------------------------------------------------------------------------------
print (length((2,4,8)))
print (pathLength3d ([(0,0,0), (1,1,1)]))  # answer is ~1.732 (square root of 3)
#print (pathLength3d (readPts ()))

# suggestion: run the code from command line
