
from collections import deque

tc = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(x, y):

    global aa
    global bb

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == aa and y == bb:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


for _ in range(tc):

    n = int(input())  # 한 변의 길이
    a, b = map(int, input().split())  # 시작 좌표
    aa, bb = map(int, input().split())  # 종료 좌표

    graph = [[0] * n for _ in range(n)]

    print(bfs(a, b))
