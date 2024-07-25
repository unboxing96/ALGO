from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque() # 0, 0 위치에서 시작
q.append((0, 0))
visited[0][0] = 1

while q:
    x, y = q.popleft()

    if x == n - 1 and y == m - 1:
        print(graph[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
            q.append((nx, ny))
            visited[nx][ny] = 1
            graph[nx][ny] = graph[x][y] + 1