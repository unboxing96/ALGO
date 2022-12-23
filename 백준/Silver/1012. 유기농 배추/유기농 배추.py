import sys
sys.setrecursionlimit(10000)

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

    def dfs(x, y):
        # 방문 처리
        graph[x][y] = 0

        # 4방 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1

    print(result)