
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if distance[nx][ny] > distance[x][y] + graph[nx][ny]:
                distance[nx][ny] = distance[x][y] + graph[nx][ny]
                q.append((nx, ny))


tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    bfs(0, 0)
    print(f"Problem {tc}: {distance[n-1][n-1]}")

    tc += 1
