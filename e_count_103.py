# 103 Johnstone UAB Fall 2016

def eCount (s):

    """Count the e's in a string, using for loop.

    Params: s (string)
    Returns: (int) #e in s, either lowercase or uppercase
    """

    # INSERT YOUR CODE HERE, replacing 'pass'
    
    count = 0
    for i in range (len(s)):
        if s[i]=='e':
            count = count + 1
        if s[i]=='E':
            count = count + 1
    return count

print (eCount ('Every Jolteon Evolved from an Eevee.')) # should return 5
