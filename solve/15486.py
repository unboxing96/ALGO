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
    
    fin_date = i + t[i] - 1
    if fin_date <= n:
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])

print(max(dp))