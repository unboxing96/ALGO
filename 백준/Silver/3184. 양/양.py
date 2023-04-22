
from collections import deque

def bfs(i, j):
    global o, v
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    if arr[i][j] == 'o':
        o += 1
    elif arr[i][j] == 'v':
        v += 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and arr[nx][ny] != '#':
                visited[nx][ny] = 1
                if arr[nx][ny] == 'o':
                    o += 1
                elif arr[nx][ny] == 'v':
                    v += 1
                q.append((nx, ny))

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = [0, 0]

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and arr[i][j] != '#':
            o, v = 0, 0
            bfs(i, j)
            if o > v:
                result[0] += o
            else:
                result[1] += v

print(result[0], result[1])