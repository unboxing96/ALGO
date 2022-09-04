import sys
sys.stdin = open("9_미로 탈출.txt", "r")

from pprint import pprint
from collections import deque

# BFS로 한 단계씩 진행하다가, (N, M) 도착하면 종료

n, m = map(int, input().split())

# 매트릭스 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 델타 좌표 (뒤로 가면 최소가 아니므로 3방향만 탐색)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
def BFS(x, y):
    # 큐 초기화 + 초기값: x, y
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향 델타 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽을 만나면 pass
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우, 현재까지 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                pprint(graph)

    return graph[n-1][m-1]

print(BFS(0, 0))