import sys
import heapq

INF = int(1e9)

n, m, start = map(int, input().split())


graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance


ans = dijkstra(start)
ans[0] = 0

for i in range(1, n + 1):
    if i != start:
        res = dijkstra(i)
        ans[i] += res[start]

print(max(ans))
