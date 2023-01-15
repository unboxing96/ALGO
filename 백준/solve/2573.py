from pprint import pprint
import sys

sys.stdin = open("2573.txt", "r")

# BFS - 4방 탐색
# 바닷물 만나면 -> 제거 그래프 ++
# 빙산 만나면 -> 큐에 추가

# 전체 그래프 탐색
# 방문하지 않고, 그래프에 값이 있으면 -> BFS 수행 후 year ++

# 전체 그래프 탐색
# 그래프에서 제거 그래프 뺴줌

# 정답 조건 확인하고
# 충족 안 되면 반복

from collections import deque


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny]:
                if graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:  # graph[nx][ny] == 0:
                    melt[x][y] += 1
    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 전체 그래프 탐색
while True:
    visited = [[0] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    ans = []

    # 방문하지 않고, 그래프에 값이 있으면 -> BFS 수행 후 year ++
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]:
                ans.append(bfs(i, j))

    # 그래프에서 제거 그래프 뺴줌
    for i in range(n):
        for j in range(m):
            graph[i][j] -= melt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(ans) == 0 or len(ans) >= 2:
        break

    year += 1

print(year) if len(ans) >= 2 else print(0)
