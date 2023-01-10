from pprint import pprint
import sys

sys.stdin = open("7576.txt", "r")

# BFS
# 그래프 생성
# 그래프 한 번 순회 -> 0 없으면 0
# 4방 탐색
# # [nx][ny] == 0: += 1
# bfs 종료되었을 때, 그래프 한 번 순회
# # 0 없으면 최소 거리 출력
# # 0 있으면 -1

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

q = deque()


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
else:
    print(result - 1)
