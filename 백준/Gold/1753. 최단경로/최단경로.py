import heapq

v, e = map(int, input().split())
start = int(input())
distance = [int(1e9)] * (v + 1)
visited = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 노드 번호, 비용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now_dist, now = heapq.heappop(q)

        # 현재 노드의 비용 > 최단 거리 테이블에 기록된 비용 -> 탐색할 필요가 없다.
        if now_dist > distance[now]:
            continue
        
        # 모든 노드의 인접 노드를 확인하며, 최단 거리 테이블 모두 갱신
        for next, next_dist in graph[now]:
            cost = now_dist + next_dist # now -> next로 거쳐가는 비용이
            if cost < distance[next]: # next에 갱신된 비용보다 작다면
                distance[next] = cost # 해당 비용으로 갱신
                heapq.heappush(q, (cost, next))

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])