import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())

dp = [0] * 10001

def fibo(x):
    if x == 0 or x == 1:
        return x
    
    elif dp[x]:
        return dp[x]
    
    dp[x] = fibo(x - 2) + fibo(x - 1)
    return dp[x]


print(fibo(n))