import heapq

def prim(start):
    hq = []
    heapq.heappush(hq, (0, start))
    visited = [0] * (n)
    result = 0

    while hq:
        now_cost, now = heapq.heappop(hq)
        if not visited[now]:
            visited[now] = 1
            result += now_cost
        
            for next_cost, next in graph[now]:
                if not visited[next]:
                    heapq.heappush(hq, (next_cost, next))

    return result

n = int(input())
nodes = []
for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((i, x, y, z)) # 노드 번호, x, y, z


graph = [[] for _ in range(n)]
for i in range(1, 3 + 1): # x, y, z축 탐색
    nodes.sort(key = lambda x : x[i]) # '인접'리스트를 만들기 위해 해당 축으로 정렬
    for j in range(n - 1): # 각 축마다 n - 1개의 인접 축 탐색
        cost = abs(nodes[j + 1][i] - nodes[j][i]) # j번 노드의 i번 축의 값 차이
        a, b = nodes[j][0], nodes[j + 1][0] # 출발 노드, 도착 노드
        graph[a].append((cost, b))
        graph[b].append((cost, a)) # 양방향 그래프

answer = prim(0)
print(answer)