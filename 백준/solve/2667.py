# DFS로 탐색
# 4방향 탐색
# dfs 수행할 때마다 cnt += 1
# dfs 종료되면 result += 1

from pprint import pprint
import sys

sys.stdin = open("2667.txt", "r")

n = int(input())

num = []

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
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
