# TestCase 개수
T = int(input())

# TestCase만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    max_tmp = -1e9

    for x in range(n):
        for y in range(m):
            tmp = matrix[x][y]
            step_range = matrix[x][y]
            for step in range(1, step_range + 1):
                for i in range(4):
                    nx = x + dx[i] * step
                    ny = y + dy[i] * step
                    if 0 <= nx < n and 0 <= ny < m:
                        tmp += matrix[nx][ny]
            max_tmp = max(max_tmp, tmp)

    print(f'#{tc} {max_tmp}')