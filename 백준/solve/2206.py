from pprint import pprint
import sys

sys.stdin = open("2206.txt", "r")

#####
# 벽을 부수는 모든 경우의 수 돌려야 할 듯
#####
from collections import deque

n, m = map(int, input().split())
graph = []

# 벽 파괴 체크를 위한 3차원 행렬
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))

    while q:
        a, b, wall = q.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][wall]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 다음 이동할 곳이 벽x and 방문한 적x
            if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[a][b][wall] + 1
                q.append((nx, ny, wall))

            # 다음 이동할 곳이 벽o and 벽 부수기 기회o
            elif graph[nx][ny] == 1 and wall == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                q.append((nx, ny, 1))

    return -1


print(bfs(0, 0, 0))
