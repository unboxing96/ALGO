from collections import deque


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            return dist[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)


n, k = map(int, input().split())

MAX = 10**5
dist = [0] * (MAX + 1)

print(bfs())