import sys

sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    x, y, xx, yy = map(int, input().split())
    for i in range(y, yy):
        for j in range(x, xx):
            graph[i][j] = 1


def dfs(x, y):

    global cnt
    cnt += 1

    graph[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            dfs(nx, ny)


cnt = 0
ans = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            dfs(i, j)
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
print(*ans, sep=" ")