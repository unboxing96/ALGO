
n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    
    print(cnt - 1)