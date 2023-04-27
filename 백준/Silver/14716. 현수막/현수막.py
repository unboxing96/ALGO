
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(start):
    
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs((i, j))
            cnt += 1

print(cnt)
