def solution(n):
    dp = [0] * (n + 1)
    return fibo(dp, n)

def fibo(dp, x):
    if x == 0 or x == 1:
        return x
    
    if dp[x]:
        return dp[x]

    dp[x] = fibo(dp, x-1) + fibo(dp, x-2)

    return dp[x]

n = int(input())
print(solution(n))