
import copy
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_res = 0


def bfs():
    # 테스트용 그래프 복사
    g = copy.deepcopy(graph)
    q = deque()

    # 값이 2인 위치 전부 큐에 추가
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == 0:
                    g[nx][ny] = 2
                    q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                cnt += 1

    global max_res
    max_res = max(max_res, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0


wall(0)
print(max_res)
