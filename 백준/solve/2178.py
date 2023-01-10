<<<<<<< HEAD
=======
# n줄 만큼 반복, 입력받아 2차원 매트릭스 생성
# 매트릭스 4방 탐색하며, BFS, 1을 만나면 원래 있던 위치의 값을 더해줌(최소 거리 찾기 위함)
# n-1, m-1에 도착하면 종료

>>>>>>> 18db6b7e1da439edb1d384f6014e540a2256fafb
import sys

sys.stdin = open("2178.txt", "r")

<<<<<<< HEAD
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

############# bfs #############

# def bfs(x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if graph[nx][ny] == 0:
#                 continue

#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))

#     return graph[n - 1][m - 1]


# print(bfs(0, 0))


################ dfs ##################
=======

n, m = map(int, input().split())

# n줄 만큼 반복, 입력받아 2차원 매트릭스 생성
graph = []
for tc in range(n):
    graph.append(list(map(int, input())))

# bfs 함수
def bfs(x, y):
    # 큐에 시작 노드를 초기화
    queue = (graph[x][y])

    while queue:
        val = queue.pop()
        if val == 1:
            

# 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 탐색
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= n and 0 <= ny <= m:
                bfs(nx, ny)


>>>>>>> 18db6b7e1da439edb1d384f6014e540a2256fafb
