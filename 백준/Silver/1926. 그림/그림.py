

from collections import deque

# dfs
def bfs(x, y):

    # 델타 탐색
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 방문 처리
    graph[x][y] = 0

    # 넓이 구하기
    length = 1

    # 큐 추가
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                length += 1
    
    return length

# 가로: m, 세로: n
n, m = map(int, input().split())

# 그래프에 데이터 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))

