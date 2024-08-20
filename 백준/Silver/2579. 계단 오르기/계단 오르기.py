n = int(input())
dp = [0] * (n + 1)
stairs = [0] * (n + 1)
for i in range(1, n+1):
    stairs[i] = int(input())

for i in range(1, n + 1):
    if i == 1:
        dp[i] = stairs[i]

    elif i == 2:
        dp[i] = stairs[i] + stairs[i-1]

    else:
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[n])