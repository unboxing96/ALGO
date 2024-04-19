import sys
sys.stdin = open("2579.txt", "r")

# 이해
# 방문하면 점수 획득
# 한 번에 1계단 혹은 2계단 이동 가능
# 연속된 3개의 계단 밟으면 안 됨.
# 시작점은 계단 X
# 마지막 계단은 반드시 밟아야 됨
# 점수의 최대값 return

# 풀이
# 마지막 계단에서 역으로 생각해보자
# 1. n, n-1, n-3 계단을 밟는다.
# 2. n, n-2 계단을 밟는다.

# dp[n] = max(dp[n-3] + stairs[n-1] + stairs[n], dp[n-2] + stairs[n-2])

n = int(input())
dp = [0] * 301
stairs = [0] * 301
for i in range(1, n+1):
    stairs[i] = int(input())

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(max(dp))