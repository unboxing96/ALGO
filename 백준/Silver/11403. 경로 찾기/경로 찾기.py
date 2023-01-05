
n = int(input())

# 2차원 그래프 무한으로 초기화
# 2차원 그래프 자기 자신으로 0으로 초기화
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for r in graph:
    print(*r, sep=" ")
