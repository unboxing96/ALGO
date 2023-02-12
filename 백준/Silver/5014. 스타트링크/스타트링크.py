
from collections import deque


def bfs():
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        x = q.popleft()

        if x == g:
            return visited[g] - 1

        for nx in [x + u, x - d]:
            if 0 < nx <= f and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
    if visited[g] == 0:
        return "use the stairs"


f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
print(bfs())
