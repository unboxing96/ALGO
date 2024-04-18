# 이해
# 1. 3으로 나누어 떨어지면 3으로 나눈다.
# 2. 2로 나누어 떨어지면 2로 나눈다.
# 3. 1을 뺀다.
# 연산 3개를 적절히 활용하여 주어진 N을 1로 만드는 연산의 최솟값을 출력하라.

# 분석
# 우선순위: 3 나누기 > 2 나누기 > 1 빼기
# 현재 인덱스를 기준으로, min([연산 수행 이전의 인덱스], [인덱스 - 1]) + 1의 값으로 갱신한다.

# 풀이
# dp = [0] * (n + 1)
# dp[1] = 1
# for i in range(2, n + 1):
    # if i % 3 == 0:
        # dp[i] = min(dp[i % 3], dp[i - 1]) + 1

def solution(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])

    return dp[n]

n = int(input())
print(solution(n))
