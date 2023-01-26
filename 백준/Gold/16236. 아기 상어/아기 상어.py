from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j


def bfs(a, b, size):

    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    eat_q = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        eat_q.append((nx, ny, distance[nx][ny]))

    return sorted(eat_q, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0
while True:
    shark = bfs(x, y, size)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    # 결과값에 현재까지 시간 추가
    result += dist

    # 먹은 위치, 상어 위치 0으로 초기화
    graph[x][y] = 0
    graph[nx][ny] = 0

    # bfs 인자값 계산
    x, y = nx, ny  # 상어 위치를 -> 먹이 위치로
    cnt += 1  # 사이즈 변경
    if cnt == size:
        cnt = 0
        size += 1

print(result)
