
from collections import deque

tc = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    graph[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))


for _ in range(tc):
    n, m, e = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a][b] = 1

    time = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                time += 1

    print(time)
