# BFS
# dx = [1, -1, *2]
# visited = []

from collections import deque


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return graph[x]

        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx <= MAX and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                q.append(nx)


n, k = map(int, input().split())
MAX = 10**5
graph = [0] * (MAX + 1)

print(bfs())
