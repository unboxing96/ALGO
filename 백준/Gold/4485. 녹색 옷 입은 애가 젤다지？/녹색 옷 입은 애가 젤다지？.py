
import heapq
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f"Problem {tc}: {distance[x][y]}")
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                ncost = graph[nx][ny] + cost

                if distance[nx][ny] > ncost:
                    distance[nx][ny] = ncost
                    heapq.heappush(q, (ncost, nx, ny))


tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    dijkstra()
    tc += 1
