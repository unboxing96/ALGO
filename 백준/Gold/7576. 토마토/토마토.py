from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

# draw graph, search graph to find 1 and append to deque
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

# 4 directions delta search with BFS,
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # where is not visited and not -1
            if graph[nx][ny] == 0:

                # record the day on graph with day variable that cnt when queue is ended
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs()

# when while is ended,
tot = 0
for g in graph:
    if 0 in g:
        print(-1)
        exit(0)
    else:
        tot = max(tot, max(g))
print(tot - 1)
# graph doesnt have any 0 -> print cnt
# graph have 0 -> print -1