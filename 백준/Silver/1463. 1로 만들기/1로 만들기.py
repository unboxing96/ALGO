n = int(input())
dp = [0] * (n + 1) # i 위치를 1로 만들기 위해 필요한 연산 횟수

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[n])