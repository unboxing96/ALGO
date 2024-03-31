# 조건
# C에서 출발하여 갱신되는 "도시의 개수, 마지막 도시가 메시지를 받는 데까지 걸리는 시간""

# 풀이
# 하나의 노드에서 출발하여 다른 모든 노드까지의 최단 경로로 도착하는 데까지 소요 시간 -> 다익스트라
# 우선순위 큐를 사용하여 풀이해보자

# C 노드에서 출발하여 현재 노드까지 최단 거리를 기록하는 distance 테이블을 Int(1e9)로 초기화 한다.
# 인접 노드 그래프를 초기화 한다.
# 힙에서 시작 노드를 추가한다. (거리: 0, 현재 노드 번호: ?)
# distance 테이블에 시작 노드를 0으로 초기화 한다.

# 큐를 반복한다.
# dist, now = 큐에서 pop한다. 
# distance 테이블 기록된 now 인덱스의 값 < dist 이라면 이미 최단 거리가 정해진 노드이니 continue
# now 노드로부터 방문 가능한 노드를 모두 탐색하며 최단 거리를 갱신할 수 있는 경우에만 갱신한다.
    # cost = distance[now] + 인접 노드까지 거리
    # if cost < distance[인접 노드]:
    # distance[인접 노드] = cost
    # 힙에 (cost, 인접 노드) push

import heapq
import sys
sys.stdin = open("전보.txt", "r")

INF = int(1e9)

def dijkstra(start):
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))



data = list(map(int, input().split()))

node_count = data[0]
edge_count = data[1]
start_node = data[2]

distance = [INF] * (node_count + 1)
linked_data = [list(map(int, input().split())) for _ in range(data[1])]
graph = [[] for _ in range(node_count + 1)]
q = []

for i in range(edge_count):
    a, b, c = linked_data[i]
    graph[a].append((b, c))

dijkstra(start_node)

cnt = 0
max_distance = 0

for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt - 1, max_distance)