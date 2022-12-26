
from collections import deque
import sys

m, n, h = map(int, input().split())

graph = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)
]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if graph[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1


queue = deque()
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1:
                queue.append((a, b, c))

bfs()

answer = 0

for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer - 1)
