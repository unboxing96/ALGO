import sys

sys.setrecursionlimit(10**8)

# 입력값 받기
n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# dfs
def dfs(x, wei):
    for a, b in graph[x]:
        if distance[a] == -1:  # 방문한 적 없으면
            distance[a] = wei + b  # distance에 가중치 더함
            dfs(a, wei + b)  # DFS


# distance 리스트 -1로 초기화
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 가장 멀리있는 노드 구하기
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
