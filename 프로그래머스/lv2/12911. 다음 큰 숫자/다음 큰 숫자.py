def solution(n):
    n에있는1개수 = bin(n).count('1')
    
    m = n + 1
    while bin(m).count('1') != n에있는1개수:
        m += 1
    
    return m