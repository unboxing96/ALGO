import sys
sys.setrecursionlimit(10000)

r, c, e = map(int, input().split())
graph = [[0] * (c+1) for _ in range(r+1)]
visited = [[False] * (c+1) for _ in range(r+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1

def dfs(x, y):
    visited[x][y] = True
    global cnt
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= r and 0 <= ny <= c:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(nx, ny)



tot = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            tot = max(tot, cnt)
print(tot)