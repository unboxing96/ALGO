# 이해
# 다익스트라로 사료된다.
# 하나의 노드로부터 모든 노드까지의 최단 거리를 구한다.
# 최단 거리에 있는 노드의 개수를 return 한다.
# 다익스트라 기본의 시간 복잡도는 O(V ** 2)이다. 시간 초과
# 다익스트라 개선의 시간 복잡도는 O(ElogV)이다. 좋다.

# 풀이
# graph 인접 그래프를 생성한다.
# vertex 정보를 입력한다.
# dist 최단 경로 테이블을 생성한다. INT의 최대값으로 초기화한다.

import heapq

INF = int(1e9)

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dijkstra(n, edge, graph, distance, 1)
    answer = distance[1:].count(max(distance[1:]))
    
    return answer


def dijkstra(n, edge, graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for neighbor in graph[now]:
            if dist + 1 < distance[neighbor]:
                distance[neighbor] = dist + 1
                heapq.heappush(q, (dist + 1, neighbor))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    