
from collections import deque

n, m, limit = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
Gram = 100000

def bfs():

    global Gram

    # 시작 노드
    q.append((0, 0))
    dist[0][0] = 1

    while len(q) > 0:
        x, y = q.popleft()

        if graph[x][y] == 2:
            Gram = n-1-x + m-1-y + dist[x][y]-1

        if x == n-1 and y == m-1:
            return min(Gram, dist[x][y] - 1)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] == 1:
                continue
            
            if dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return Gram


result = bfs()
print("Fail" if result > limit else result)