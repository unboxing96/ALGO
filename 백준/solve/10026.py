from pprint import pprint
import sys

sys.stdin = open("10026.txt", "r")

# 일반인
# 입력 들어온 값으로 bfs 시작
## 같은 문자 반복하고
## bfs 끝나면 result += 1

# 색맹
# graph를 B나 R로 replace
## 같은 문자 반복하고
## bfs 끝나면 result += 1

from collections import deque


def bfs(x, y):
    # 방문한 문자 저장
    now = graph[x][y]

    # 방문 처리
    graph[x][y] = 0

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == now:
                q.append((nx, ny))
                graph[nx][ny] = 0


def new_bfs(x, y):
    # 방문한 문자 저장
    now = new_graph[x][y]

    # 방문 처리
    new_graph[x][y] = 0

    q = deque()
    q.append((x, y))

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if new_graph[nx][ny] == 0:
                continue

            if new_graph[nx][ny] == now:
                q.append((nx, ny))
                new_graph[nx][ny] = 0


n = int(input())

graph = []
new_graph = []
for _ in range(n):
    temp = input()
    graph.append(list(temp))
    new_graph.append(list(temp.replace("R", "G")))

result = 0
new_result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs(i, j)
            result += 1

        if new_graph[i][j] != 0:
            new_bfs(i, j)
            new_result += 1

print(result, new_result)
