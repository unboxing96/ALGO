import heapq


def dijkstra(n, start, end, graph):
    distance = [int(1e9) for _ in range(n + 1)]

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # (거리, 노드)로 저장된 큐에서 pop
        d, now = heapq.heappop(q)

        # 새롭게 뽑아낸 노드의 거리가, 기존에 저장된 거리보다 오래 걸리면, continue
        if distance[now] < d:
            continue

        # 갱신할 가치가 있으면, 해당 노드의 인접 노드를 뽑아서,
        for next_node, next_cost in graph[now]:
            # 인접 노드의 가중치 + 뽑아낸 거리가, 기존 저장된 인접 노드 거리보다 빠르면, 갱신
            cost = d + next_cost
            if distance[next_node] > cost:
                distance[next_node] = cost
                # 인접 노드의 거리, 다음 인접 노드 append
                heapq.heappush(q, (cost, next_node))

    return distance[end]


def solution(n, s, a, b, fares):

    graph = [[] for _ in range(n + 1)]

    for i, j, cost in fares:
        graph[i].append((j, cost))
        graph[j].append((i, cost))

    result = []
    for p in range(1, n + 1):
        if p != s:
            s_to_p = dijkstra(n, s, p, graph)
            p_to_a = dijkstra(n, p, a, graph)
            p_to_b = dijkstra(n, p, b, graph)
            result.append(s_to_p + p_to_a + p_to_b)
        else:
            result.append(dijkstra(n, s, a, graph) + dijkstra(n, s, b, graph))

    return min(result)
