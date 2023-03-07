import sys
sys.stdin = open("2146.txt", "r")

"""
1. color different space with different name
2. Do brute force. find path from one to another with BFS
"""
from pprint import pprint
from collections import deque
import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
color = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, col):
    q = deque()
    q.append((i, j))
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    color[nx][ny] = col
                    q.append((nx, ny))

def find_path(i, j):
    q = deque()
    q.append((i, j))
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True
    now = 0

    while q:
        x, y = q.popleft()

        if color[x][y] != now:
            return graph[x][y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and color[nx][ny]:
                    now = color[nx][ny]
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


# color with different name
col = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            col += 1
            bfs(i, j, col)

# 2. Do brute force. find path from one to another with BFS
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            res.append(find_path(i, j))

print(min(res))