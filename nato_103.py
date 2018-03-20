# 103 Johnstone UAB Fall 2016

# ------------------------------------------------------------------------------
# helper function: read but do not touch
def readFileIntoWordList (f):

    """Read a file into a list of words.

    This is a helper function for 'toNatoAlphabet'.
    DO NOT CHANGE ME.

    Params: f (string): filename
    Returns: (list of strings) words in the file
    """

    return open (f).read().split()

"""
download the file 'NATO_phonetic_alphabet.txt' from
CS103's Canvas files: Files > hw0
to the same directory as this code;
to look at this file,
from Windows command line: type NATO_phonetic_alphabet.txt | more
from Unix (Apple) command line: more NATO_phonetic_alphabet.txt
"""
# helper code: read but do not touch
nato_alphabet = readFileIntoWordList ('NATO_phonetic_alphabet.txt')

# ------------------------------------------------------------------------------
# here is the function you will work with

def toNatoAlphabet (w, nato):
    
    """Spell a word using the NATO Phonetic Alphabet.

    Example: 'bar' -> 'Bravo Alpha Romeo'
             'CS103' -> 'Charlie Sierra One Zero Three'
    Reference: https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

    Note: this code does not need to be long.
    My solution is 6 lines long.

    Params: 
        w (string): word consisting only of alphabetic letters and numbers
        nato (list): NATO phonetic alphabet, sorted (letters first, numbers 2nd)
    Returns: (string) NATO phonetic alphabet spelling of this text
    """

    # INSERT YOUR CODE HERE, replacing 'pass'
    pass

print (repr (toNatoAlphabet ('bar', nato_alphabet)))
# it will be easier to debug using repr, which reveals more about the string
