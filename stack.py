# Terrance Blount
L = [5,4,3,2,1]
def push(s):
    s.append(L)
    
def isEmpty(s):
    if s == []:
        return True
    else:
        return False
        
def top(s):
    return s[0]
    
def nextToTop(s):
    return s[1]
    
print(push(L))
print(isEmpty(L))
print(top(L))
print(nextToTop(L))
    
    
