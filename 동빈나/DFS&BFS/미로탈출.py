import sys
from collections import deque
sys.stdin = open("미로탈출.txt", "r")

# 괴물은 0
# 목적지까지 최소 이동 칸의 수
# 시작과 도착 지점도 cnt
# BFS, 4방향 탐색

r, c = map(int, input().split())
graph = [list(map(int, input())) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[r-1][c-1]

print(bfs(0, 0))