from collections import deque

INF = 100001
n, k = map(int, input().split())
graph = [int(1e9)] * INF


def bfs():
    graph[n] = 0
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()

        if v == k:
            return graph[k]

        for nv in [v + 1, v - 1, v * 2]:
            if 0 <= nv < INF:
                if graph[nv] >= graph[v] + 1:
                    graph[nv] = graph[v] + 1
                    q.append(nv)


print(bfs())