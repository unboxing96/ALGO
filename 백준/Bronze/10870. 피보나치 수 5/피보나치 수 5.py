import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
dp = [0] * (n + 1)

def fibo(x):

    if x == 0:
        return 0

    if x == 1 or x == 2:
        return 1
    
    if dp[x]:
        return dp[x]
    
    return fibo(x - 1) + fibo(x - 2)

print(fibo(n))