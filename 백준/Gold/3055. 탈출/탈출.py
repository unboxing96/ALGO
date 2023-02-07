from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def bfs(sx, sy):
    while q:

        if graph[sx][sy] == "S":
            return visited[sx][sy]

        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] == "." or graph[nx][ny] =="D") and graph[x][y] == "S":
                    visited[nx][ny] = visited[x][y] + 1
                    graph[nx][ny] = "S"
                    q.append((nx, ny))
                elif (graph[nx][ny] == "S" or graph[nx][ny] == ".") and graph[x][y] == "*":
                    graph[nx][ny] = "*"
                    q.append((nx, ny))

    return "KAKTUS"


for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            q.append((i, j))
        elif graph[i][j] == "D":
            sx, sy = i, j

for i in range(r):
    for j in range(c):
        if graph[i][j] == "*":
            q.append((i, j))

print(bfs(sx, sy))