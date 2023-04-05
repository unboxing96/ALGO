
from collections import deque

r, c = map(int, input().split())
graph = [input() for _ in range(r)]
fire_visited = [[0] * c for _ in range(r)]
jihun_visited = [[0] * c for _ in range(r)]
fire_q = deque()
jihun_q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 위치 찾기
for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            jihun_q.append((i, j))
            jihun_visited[i][j] = 1

        elif graph[i][j] == "F":
            fire_q.append((i, j))
            fire_visited[i][j] = 1

def fire_bfs():
    while fire_q:
        x, y = fire_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < r and 0 <= ny < c):
                continue
            
            if fire_visited[nx][ny] or graph[nx][ny] == "#":
                continue

            fire_visited[nx][ny] = fire_visited[x][y] + 1
            fire_q.append((nx, ny))

def jihun_bfs():
    while jihun_q:
        x, y = jihun_q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < r and 0 <= ny < c):
                print(jihun_visited[x][y])
                return
            
            if jihun_visited[nx][ny] or graph[nx][ny] == "#":
                continue

            if fire_visited[nx][ny] and fire_visited[nx][ny] <= jihun_visited[x][y] + 1:
                continue

            jihun_visited[nx][ny] = jihun_visited[x][y] + 1
            jihun_q.append((nx, ny))
    
    print("IMPOSSIBLE")
    return


fire_bfs()
jihun_bfs()