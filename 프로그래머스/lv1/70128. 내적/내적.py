def solution(a, b):
    
    size = len(a)
    tot = 0
    
    for i in range(size):
        tot += a[i] * b[i]
    
    return tot