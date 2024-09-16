import heapq

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start, 0)) # cost, node, wrap_up_cnt
    distance[start][0] = 0

    while hq:
        now_cost, now, wrap_up_cnt = heapq.heappop(hq)
        if now_cost > distance[now][wrap_up_cnt]:
            continue
        for next_cost, next in graph[now]:
            new_cost = now_cost + next_cost
            # 포장X
            if distance[next][wrap_up_cnt] > new_cost:
                distance[next][wrap_up_cnt] = new_cost
                heapq.heappush(hq, (new_cost, next, wrap_up_cnt))
            # 포장O
            # 포장하는 경우 다음 노드 이동 비용이 0 -> now_cost를 그대로 사용
            if wrap_up_cnt < k and distance[next][wrap_up_cnt + 1] > now_cost:
                distance[next][wrap_up_cnt + 1] = now_cost
                heapq.heappush(hq, (now_cost, next, wrap_up_cnt + 1))


INF = int(5 * 1e10 + 1)
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a)) # 양방향 그래프

distance = [[INF] * (k + 1) for _ in range(n + 1)]

dijkstra(1)
print(min(distance[n]))