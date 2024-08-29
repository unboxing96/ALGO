
n = int(input())
arr = [0] * 301
for i in range(1, n + 1):
    arr[i] = int(input())

dp = [0] * 301 # 해당 인덱스를 밟고 있는 경우, 해당 인덱스까지의 최댓값
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
for i in range(4, n + 1):
    dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2])

print(dp[n])