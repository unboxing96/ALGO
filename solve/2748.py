import sys
sys.stdin = open("2748.txt", "r")

# 이해
# 피보나치 수열
# 점화식은 dp[i] = dp[i - 1] + dp[i - 2]
# dp[0] = 0
# dp[1] = 1
# dp[n]을 출력한다.

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