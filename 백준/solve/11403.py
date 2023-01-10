import sys

sys.stdin = open("11403.txt", "r")

# 2차원 그래프 무한으로 초기화
# 2차원 그래프 자기 자신으로 0으로 초기화
# 입력값 그래프에 입력
# 3중 반복하며 플로이드 워셜 진행
# 2차원 그래프 순회하며 출력

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
