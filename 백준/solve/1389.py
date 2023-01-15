import sys

sys.stdin = open("1389.txt", "r")

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    cnt = [0] * (n + 1)
    visited = [start]
    q = deque()
    q.append(start)

    while q:
        qq = q.popleft()
        for i in graph[qq]:
            if i not in visited:
                visited.append(i)  # 방문 처리
                cnt[i] = cnt[qq] + 1  # 거리 계산
                q.append(i)  # 큐에 추가

    return sum(cnt)


result = []
for i in range(1, n + 1):
    result.append(bfs(i))

print(result.index(min(result)) + 1)
