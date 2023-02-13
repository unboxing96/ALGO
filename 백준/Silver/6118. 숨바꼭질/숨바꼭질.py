from collections import deque

v, e = map(int, input().split())


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


visited = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()

max_dis = max(visited)
max_cnt = visited.count(max_dis)
max_idx = visited.index(max_dis)

print(max_idx, max_dis - 1, max_cnt)
