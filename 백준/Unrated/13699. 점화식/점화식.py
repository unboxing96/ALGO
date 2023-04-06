import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())

dp = [0] * 36

def fibo(x):
    if x == 0 or x == 1:
        return 1
    
    elif dp[x]:
        return dp[x]
    
    tmp = 0
    for i in range(x):
        num = fibo(i) * fibo(x - i - 1)
        tmp += num

    dp[x] = tmp
    return dp[x]

print(fibo(n))