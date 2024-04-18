import sys
sys.stdin = open("15486.txt", "r")

n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    finish_date = i + t[i] - 1
    
    if finish_date <= n:
        dp[finish_date] = max(dp[finish_date], dp[i - 1] + p[i])

print(max(dp))