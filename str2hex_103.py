# 103 Johnstone UAB Fall 2016

def char2binary (c):

    """Translate a character to the binary encoding of its Unicode code point.

    Example: 'a' --> 1100001
    Hint: recall the ord function mentioned in lecture Thursday
    (see https://docs.python.org/3/library/functions.html)

    Params: c (str of length 1) a character
    Returns: (str) binary encoding of c's Unicode code point, 
                   with no leading '0b'
    """

    # INSERT CODE HERE

    c = ord(c)
    
    return bin(c)[2:]
    
def str2binary (s):

    """Translate a string to binary.

    Example: 'Joe' -> 100101011011111100101
    
    Params: s (str): 
    Returns: (str) a binary encoding of this string (as defined above);
                   with no leading '0b'
    """

    # INSERT CODE HERE
    
    x = ''
    
    for i in s:
        x = x + char2binary(i)
        
    return x

def binary2hex (b):

    """Translate a binary number to hexadecimal.
    
    Example: '111100' --> '3c'
             '10001'  --> '11'

    Params: b (str): string representing a binary number with no leading '0b'
                     (e.g., '111100')
    Returns: (str) string representing its hexadecimal equivalent
    """
    
    # INSERT CODE HERE
    x = int(b ,2)
    
    b = hex(x)
    
    return b[2:]
    

def str2hex (name):

    """Translate a string to hexadecimal.

    Algorithm:
    - first translate the name to binary, as above
    - then translate this binary number to hexadecimal, as above

    Params: name (str): someone's name (e.g., 'Mary')
    Returns: (str) an hexadecimal encoding of this name
    Raises: ValueError if parameter is not a string with only one word
            with the diagnostic message
            'str2hex parameter should be a string with one word'
            for example, 'Alan Turing' would raise a ValueError,
            but 'Alan' would not
    """

    # INSERT CODE HERE
    # make sure to use the helper functions char2binary, str2binary, binary2hex,
    # directly or indirectly
    
    x = str2binary(name)
    c = binary2hex(x)
    
    return c


# test data
print ('Joe bin =', str2binary ('Joe')) # should return '100101011011111100101'
print ('Joe',       str2hex ('Joe'))    # should return '12b7e5'
print ('Mary =',    str2hex ('Mary'))   # should return '9b87979'

# grading data
print ('Grace =',   str2hex ('Grace'))
print ('Alan  =',   str2hex ('Alan'))
print ('Terrance   =',   str2hex ('Terrance'))    # replace XXX by your first name
print ('Error =',   str2hex ('Frank Mahovlich'))
