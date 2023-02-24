from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))


def bfs():

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


bfs()

for row in graph:
    for elem in row:
        if elem == 0:
            print(-1)
            exit(0)
    res = max(res, max(row))
print(res - 1)
