<<<<<<< HEAD
# DFS로 탐색
# 4방향 탐색
# dfs 수행할 때마다 cnt += 1
# dfs 종료되면 result += 1

from pprint import pprint
=======
from collections import deque
>>>>>>> 18db6b7e1da439edb1d384f6014e540a2256fafb
import sys

sys.stdin = open("2667.txt", "r")

n = int(input())

<<<<<<< HEAD
num = []

=======
>>>>>>> 18db6b7e1da439edb1d384f6014e540a2256fafb
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

<<<<<<< HEAD
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

=======

def bfs(graph, a, b):
    n = len(graph)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((a, b))

    # 방문 처리
    graph[a][b] = 0
    # bfs 시작하면서, cnt = 1 초기화
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
>>>>>>> 18db6b7e1da439edb1d384f6014e540a2256fafb
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
<<<<<<< HEAD
                return False

            else:
                dfs(nx, ny)
        return True
    return False


cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
print(*num, sep="\n")
=======
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


tot = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            tot.append(bfs(graph, i, j))

tot.sort()
print(len(tot))
print(*tot, sep="\n")
>>>>>>> 18db6b7e1da439edb1d384f6014e540a2256fafb
