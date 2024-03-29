from pprint import pprint


# 6방향 탐색 bfs (3차원 범위 설정 주의)
# 그래프 생성
# visited 배열 생성
# 1을 값으로 갖는 그래프 위치 queue에 append
# 모든 토마토가 1이면 0 출력
# 가장 큰 값 -= 1
# 익지 않은 토마토(0) 있으면 -1 출력


from collections import deque
import sys

sys.stdin = open("7569.txt", "r")

m, n, h = map(int, input().split())

graph = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)
]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = True


queue = deque()
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a, b, c))
                visited[a][b][c] = True

bfs()

answer = 0

for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer - 1)
