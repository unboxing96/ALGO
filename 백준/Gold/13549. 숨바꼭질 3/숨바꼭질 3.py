from collections import deque

n, k = map(int, input().split())

MAX_CNT = 100001
visited = [0] * MAX_CNT


def bfs(n, k):
    visited[n] = 1
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return visited[k] - 1

        for nx in [x + 1, x - 1, 2 * x]:
            if 0 <= nx < MAX_CNT and (not visited[nx] or visited[nx] >= visited[x] + 1):
                if nx == 2 * x:
                    visited[nx] = visited[x]
                    q.append(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


print(bfs(n, k))