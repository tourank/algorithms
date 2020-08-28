def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

def unique_paths(m,n):
    R = m-1
    D = n-1
    total = R + D
    result = fact(total)//(fact(R)*fact(D))
    return result 

print(unique_paths(7,3))
    
