import sys
sys.stdin = open("1504.txt", "r")

import heapq
import sys

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    q = []
    distance = [int(1e9) for _ in range(n + 1)]
    heapq.heappush(q, (0, start))   # 시작점부터 시작점까지 거리(0), 시작점 노드(1)
    distance[start] = 0             # 시작점부터 시작점까지 거리를 0으로

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, next_cost in graph[node]: # 인접노드 탐색
            cost = distance[node] + next_cost
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    
    return distance[end]

route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if route1 == int(1e9) and route2 == int(1e9):
    print(-1)
else:
    print(min(route1, route2))