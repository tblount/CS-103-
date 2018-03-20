# 103 Johnstone UAB Fall 2016

def countConsonant (s):

    """Count consonants.

    'y' and 'Y' are not consonants.

    Params: s (string)
    Returns: (int) #consonants in s (either case)
    """

    # do not use a brute force solution:
    # think of a short elegant solution (mine is 5 lines long);
    # do not use lines longer than 80 characters long

    # INSERT YOUR CODE HERE, replacing 'pass'
    
    count = 0
    vowel = ('')
    other = '',',','.','""'
    for i in range (len(s)):
        if s[i]==(vowel):
            count = 0
        elif s[i]==other:
            count = 0
        else:
            count = count + 1
        
    return count

print (countConsonant ('"Carpe diem", every day.')) # should return 8


