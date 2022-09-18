n = int(input())
s, e = map(int, input().split())
edge = int(input())

graph = [ [] for _ in range(n + 1) ]
visited = [0] * (n + 1)
result = []

for _ in range(edge):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, num):
    num += 1
    visited[start] = 1

    if start == e:
        return result.append(num)

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, num)

dfs(s, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
