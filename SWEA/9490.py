import sys
sys.stdin = open("9490.txt")

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_cnt = 0

    for x in range(n):
        for y in range(m):
            tmp_cnt = matrix[x][y]
            for weight in range(1, matrix[x][y] + 1):
                for i in range(4):
                    nx = x + dx[i] * weight
                    ny = y + dy[i] * weight
                    if 0 <= nx < n and 0 <= ny < m:
                        tmp_cnt += matrix[nx][ny]

            max_cnt = max(max_cnt, tmp_cnt)
    
    print(f"#{tc} {max_cnt}")



