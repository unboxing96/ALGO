# 유형: 플로이드 워셜
# 1에서 출발하여 k를 거쳐 x로 도착.
# 전체 리스트를 갱신할 필요는 없고, k를 거쳐서 x로 도착하는 경우의 값만 필요

# 플로이드 워셜
# 전체 그래프를 INF로 초기화
# 출발 위치와 도착 위치가 같은 경우 0으로 갱신
# k -> a -> b 순서로 탐색하며, min([a][b], [a][k]+[k][b])로 모두 갱신
# 현재 문제에서는 1 -> k -> x로 가는 최소 시간이 필요하므로, 그냥 [1][k]+[k][b]

import sys
sys.stdin = open("미래도시.txt", "r")

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][k] + graph[k][x]

print(-1 if distance >= INF else distance)