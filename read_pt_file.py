def randPt2 ():

    """Random point in 2-space.

    Returns: (2-tuple, a tuple of size 2): random point in 2-space
    """

    # INSERT CODE HERE
    pass

def writeRandomPts (n, f):
    
    """Write n random points in 2-space to a file.

    To refresh on files and file input,
    read the code on Canvas (under Files/illustrative_code/file_input)
    and perhaps the slides on file input (Files/lecture_slides, in Lecture 7)

    Open the file in write mode (very similar to opening a file in read mode.)
    Generate a lot of random points in 2-space 
    (perhaps in a 100x100 square, but your choice)
    immediately writing each one out to the file.
    To read from a file with file handle f, we use f.read().
    To write to a file with file handle f, we use f.write(string).
    The file does not need to exist: actually, if it does, it overwrites it!
    Note that the write function expects a string parameter,
    so everything you write must be cast to a string first.

    Params: 
        n (int): how many random points to generate?
        f (string): filename to write 
    """

    # INSERT CODE HERE
    pass


def readAndChoose (i, f):

    """Choose a point from a file of points in 2-space.

    Params: 
        i (int): which point to choose (its index, so 0 => first)
        f (string): name of a file of points in 2-space
    Returns: (tuple) ith point in that file
    """

    # INSERT CODE HERE
    pass

writeRandomPts (100, 'pts.dat')
print (readAndChoose (10, 'pts.dat'))


