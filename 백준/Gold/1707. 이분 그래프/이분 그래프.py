
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:  # 방문하지 않은 곳이라면
                q.append(i)
                visited[i] = -1 * visited[x]  # 다른 그룹 처리
            elif visited[i] == visited[x]:  # 이미 방문했고 + 같은 그룹이라면
                return False
            # 방문했는데 + 다른 그룹이라면
    return True


n = int(input())
for tc in range(n):
    node, edge = map(int, input().split())
    graph = [[] for _ in range(node + 1)]
    visited = [0] * (node + 1)

    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, node + 1):
        if not visited[i]:
            result = bfs(i)
            if not result:
                break

    print("YES" if result else "NO")
