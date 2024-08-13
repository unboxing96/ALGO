# 문제 분석
# 입력값이 특이하다. x, y, w, h
    # x, y 좌표를 반대로 해야 직관적이다.

n = int(input())
matrix = [[0] * 1001 for _ in range(1001)]
count_arr = [0] * (n + 1)

for tc in range(n):
    y, x, h, w = map(int, input().split())
    for i in range(w):
        for j in range(h):
            matrix[x + i][y + j] = tc + 1

for i in range(1001):
    for j in range(1001):
        if matrix[i][j] != 0:
            count_arr[matrix[i][j]] += 1

for i in range(1, len(count_arr)):
    print(count_arr[i])