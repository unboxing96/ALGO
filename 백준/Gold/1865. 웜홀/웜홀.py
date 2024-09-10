INF = int(1e9)

def bf(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    for i in range(n):  # 노드 개수만큼 반복
        for j in range(len(edges)):  # 각 노드마다 모든 간선 확인
            cur_node, next_node, edge_cost = edges[j]
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == n - 1:  # n번째 노드에서도 갱신이 된다면 -> 음수 순환이 존재하는 것
                    return "YES"
    return "NO"

T = int(input())
for _ in range(1, T + 1):
    n, m, w = map(int, input().split())  # 노드, 간선, 웜홀 개수
    edges = []

    for _ in range(m):  # 간선
        a, b, c = map(int, input().split())
        edges.append((a, b, c))  # a -> b, 비용: c
        edges.append((b, a, c))  # b -> a, 비용: c (양방향 간선)

    for _ in range(w):  # 웜홀
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))  # a -> b, 비용: -c (단방향 웜홀)

    print(bf(1))