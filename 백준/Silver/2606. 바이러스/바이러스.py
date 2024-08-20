v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):

    global cnt
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            dfs(node)
            cnt += 1

cnt = 0
dfs(1)
print(cnt)