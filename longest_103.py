# 103 Johnstone UAB Fall 2016

def longest (s1, s2, s3):

    """Longest of three strings.

    You may assume that the longest string is unique.
    (What would you do if it wasn't?)

    Params:
        s1 (string)
        s2 (string)
        s3 (string)
    Returns: (string) longest string
    """

    # INSERT YOUR CODE HERE, replacing 'pass'
    
    s1 = ''
    s2 = ''
    s3 = ''
    
    if s2[:] > s1[:]:
        return s2
    else:
        return s3
        

print(longest ('elegant', 'is', 'code')) # should return 'elegant'
#print (longest ('is', 'elegant', 'code')) # should return 'elegant'
#print (longest ('is', 'code', 'elegant')) # should return 'elegant'
