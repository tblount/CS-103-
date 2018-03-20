# 103 Johnstone UAB Fall 2016

def lastFirst (s):

    """Last letter of first word.

    You may assume that words of the string are separated by spaces.

    Params: s (string) 
    Returns: (string) last letter of first word
    """
    
    for index in range(len(s)):
        if s[index]=="":
            return s[-1]

print (lastFirst ('to code or not to code'))
print (lastFirst ('It was the best of times, it was the worst of times.'))

