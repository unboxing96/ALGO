import sys
sys.stdin = open("9372.txt", "r")

def dfs(x):
    visited[x] = True
    global cnt
    cnt += 1

    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(cnt - 1)