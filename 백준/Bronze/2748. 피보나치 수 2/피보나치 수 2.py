# 이해
# 피보나치 수열
# 점화식은 dp[i] = dp[i - 1] + dp[i - 2]
# dp[0] = 0
# dp[1] = 1
# dp[n]을 출력한다.

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = int(input())
print(solution(n))