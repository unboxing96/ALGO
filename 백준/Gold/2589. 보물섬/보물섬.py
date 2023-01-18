
from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()


def bfs(i, j):

    visited = [[0] * m for _ in range(n)]
    visited[i][j] += 1
    q.append((i, j))
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == "L" and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                cnt = max(cnt, visited[nx][ny])

    return cnt - 1


# 모든 L 위치 큐에 넣어줌
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)
