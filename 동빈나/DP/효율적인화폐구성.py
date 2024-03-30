# 최적 부분 구조
    # 맞다. 특정 값을 구성하기 위한 최소 화폐 개수는 정해져 있다.
# 중복되는 부분 문제
    # 해당 구조가 여러 번 반복된다.


# 풀이
# 무조건 고액 화폐를 많이 사용하는 것이 옳은가?
# 그렇지 않다. 700을 고려해보자. 300 + 300 + ...? / 300 + 200 + 200
# 1로 만들기 문제처럼, 100부터 목표 값까지 최소 화폐 개수를 채워나가보자.
# coins = [200, 300]
# [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# [  0,   1,   1,   2,   2,   2,   3,   3,   3,    4]
# 쉬운 듯?
# min(Sn-300 + 1, Sn-200 + 1)

# if 조건문으로 모든 케이스를 검증하며 풀이해보자. 아니다. 조건문조차 필요가 없다.
# dp = [0] * 10001

# for coin in coins:
# dp[coin] = 1

# for i in range(min(coins), m + 1)
    # for coin in coins:
        # if i > coin:
            # dp[i] = min(dp[i], dp[i - coin] + 1)

# -1 if dp[m] == 1 else dp[m]


import sys
sys.stdin = open("효율적인화폐구성.txt", "r")

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n): # 화폐 단위
    for j in range(coins[i], m+1): # 목표 금액
        if dp[j - coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coins[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

