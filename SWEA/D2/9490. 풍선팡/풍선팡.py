# 문제 분석
# 풍선에 들어있는 개수만큼 상하좌우

# TestCase 개수
T = int(input())

# TestCase만큼 반복
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, -1, 0]  # 우, 하, 좌, 상
    dy = [1, 0, 0, -1]
    max_value = -1e9

    for x in range(N):
        for y in range(M):
            tmp = matrix[x][y]
            poong = matrix[x][y]
            for i in range(4):
                for step in range(1, poong + 1):
                    nx = x + dx[i] * step
                    ny = y + dy[i] * step

                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue

                    tmp += matrix[nx][ny]

            if max_value < tmp:
                max_value = tmp

    print(f'#{tc} {max_value}')
