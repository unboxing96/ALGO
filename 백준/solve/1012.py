# 전체 행렬 순회
# 행렬 값이 1이면, dfs/bfs 시작
# # dfs/bfs 시작하면 방문 처리 (1 -> 0)
# # 4방 탐색
# # nx,ny 행렬 값이 1이고, 행렬 범위에서 벗어나지 않으면
# # dfs/bfs
# dfs/bfs 끝나면,
# result += 1
# 전체 행렬 순회 끝나면,
# print(result)

from pprint import pprint
import sys

sys.stdin = open("1012.txt", "r")

from collections import deque


t = int(input())

for tc in range(t):

    n, m, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    result = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(a, b):
        # 방문 처리
        graph[a][b] = 0

        q = deque()
        q.append((a, b))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)

    # def dfs(x, y):
    #     # 방문 처리
    #     graph[x][y] = 0

    #     # 4방 탐색
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]

    #         if nx < 0 or nx >= n or ny < 0 or ny >= m:
    #             continue

    #         if graph[nx][ny] == 1:
    #             dfs(nx, ny)

    # for i in range(n):
    #     for j in range(m):
    #         if graph[i][j] == 1:
    #             dfs(i, j)
    #             result += 1

    # print(result)
