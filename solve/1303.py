import sys
sys.stdin = open("1303.txt", "r")
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    visited[x][y] = True
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if not visited[nx][ny] and matrix[nx][ny] == matrix[x][y]:
            cnt += dfs(nx, ny)
    
    return cnt

c, r = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

w = 0
b = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            tmp = dfs(i, j)
            if matrix[i][j] == "W":
                w += tmp ** 2
            else:
                b += tmp ** 2

print(w, b)
