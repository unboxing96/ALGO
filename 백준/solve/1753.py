from pprint import pprint

import sys

sys.stdin = open("1753.txt", "r")

# 다익스트라
# 시작 지점 초기화
# 인접 노드 그래프 초기화
# 최단 거리 기록 리스트 초기화
# 우선 순위 큐에서 "최소 거리" 기준으로 heappop
# pop한 노드의 인접 노드 순회
# # 최소 거리 변경
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

# 인접 노드 그래프 초기화
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 최단 거리 기록 리스트 초기화
distance = [INF] * (v + 1)


def dijkstra(start):
    q = []  # 우선순위 큐 초기화
    heapq.heappush(q, (0, start))  # start 노드 지정
    distance[start] = 0  # 자기 자신으로의 거리는 0으로

    while q:
        dist, now = heapq.heappop(q)  # 최소 거리가 가장 짧은 (노드) + 시작 지점부터 (최소 거리) pop

        # 기존 최소 거리 < 이전 지점를 거친 최소 거리 -> 제외 (이미 방문했기 때문)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
