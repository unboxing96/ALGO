n = int(input())
m = int(input())

visited = [0] * (n + 1)

graph = [ [] * n for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

# DFS
def DFS(start):
    global cnt
    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            DFS(i)
            cnt += 1

DFS(1)
print(cnt)