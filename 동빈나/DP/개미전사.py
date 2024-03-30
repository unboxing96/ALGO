# DP인지 판단
# 최적 부분 구조가 가능한가?
    # 특정 구간의 최대 조합이 있을 것이다. 그것은 구간을 확장해도 조합이 바뀌지 않을 것이다.
# 중복되는 부분 문제가 있는가?
    # 특정 구간의 조합이 다음 구간에 영향을 주므로 (1칸 이상 떨어져야 함) 중복되는 문제가 있다고 보아야 한다.

# 메모이제이션 - 탑 다운으로 풀이해보자
# 배열의 크기가 1일 때는? a1
# 2일 때는? max(S1, a2)
# 3일 때는? max(S2, S1 + a3)
# 4일 때는? max(S3, S2 + a4)
# 5일 때는? max(S4, S3 + a5)
# 6일 때는? max(S5, S4 + a6)
# n일 때는? max(Sn-1, Sn-2 + an)
# S1 = arr[0]
# S2 = max(arr[1], arr[0])
# Sn = max(Sn-1, Sn-2 + an)

import sys
sys.stdin = open("개미전사.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 10
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

def get_food(n):

    if dp[n] != 0:
        return dp[n]
    
    dp[n] = max(dp[n - 1], dp[n - 2] + arr[n])

    return dp[n]

print(get_food(n - 1))
print(dp)