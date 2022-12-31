from collections import deque
import sys

sys.stdin = open("2667.txt", "r")

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(graph, a, b):
    n = len(graph)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((a, b))

    # 방문 처리
    graph[a][b] = 0
    # bfs 시작하면서, cnt = 1 초기화
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


tot = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            tot.append(bfs(graph, i, j))

tot.sort()
print(len(tot))
print(*tot, sep="\n")
