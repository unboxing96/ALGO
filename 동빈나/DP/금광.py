# 최적 부분 구조
    # 맞다. 전체의 문제를 한 열씩 나눠서 판단할 수 있다. 
    # 특정 구간 최적 경로는 전체 구간에서 봐도 그렇다.
# 중복되는 부분 문제
    # 하나의 최적 경로를 구하는 문제이므로, 같은 구간이 중복되어 계산된다.

# 풀이
# 무작정 3방향 중 최대값을 선택하면 되는가?
# 안 된다. 그건 그리디이다. 이동 범위 밖에 있는 최적 경로가 존재할 수 있다.

# 전체 행에서 최대값을 선택하는 것도 불가능하다. 이동이 불가능할 수도 있으므로.

# 2차원 배열을 탐색하며 이전 3방향의 최대값을 더해주는 방식으로 배열을 갱신해야겠다.
# 현재 인덱스의 값은, 이전 3방향 값 중 최대값을 더한 값이다.
# 즉, 다음과 같다.
# dp[i][j] = dp[i - 1][j] +  matrix[i][j-1]
# if i > 0:
# dp[i][j] = max(dp[i][j], dp[i-1][j-1] + matrix[i][j])
# if i + 1 < n 
# dp[i][j] = max(dp[i][j], dp[i+1][j-1] + matrix[i][j])


import sys
sys.stdin = open("금광.txt", "r")

tc = int(input())

for k in range(tc):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    matrix = []
    for i in range(0, len(arr), m):
        matrix.append(arr[i : i + m])

    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = matrix[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            
            left = dp[i][j - 1]
            dp[i][j] = matrix[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)

    # 1 3 1 5
    # 2 2 4 1
    # 5 0 2 3
    # 0 6 1 2

    # 1 5 8 5
    # 2 7 11 1
    # 5 5 13 3
    # 0 11 6 2