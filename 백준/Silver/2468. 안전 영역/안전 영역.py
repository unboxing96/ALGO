import sys

sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

height = 0
for i in graph:
    height = max(height, max(i))


def dfs(x, y):

    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] > h and visited[nx][ny] == 0:
            dfs(nx, ny)


temp_list = []
for h in range(height):
    temp = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                dfs(i, j)
                temp += 1
    temp_list.append(temp)

print(max(temp_list))
