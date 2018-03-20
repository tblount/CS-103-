# 103 Johnstone UAB Fall 2016

import string                                               # you will need this

def isPunct (s):
    
    """Determine if a character is punctuation.

    Params: s (string) a single character (len(s) == 1)
    Returns: (bool) is this a punctuation character?
    """

    if s in string.punctuation:
        return True
    else :
        return False 

print (isPunct ('a')) 
print (isPunct ('.')) 

