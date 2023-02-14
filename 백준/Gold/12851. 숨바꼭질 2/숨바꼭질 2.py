from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
cnt = 0


def bfs(n, k):
    global cnt
    visited[n] = 1
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            cnt += 1

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx < 100001:
                if not visited[nx] or visited[nx] >= visited[x] + 1:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


bfs(n, k)
print(visited[k] - 1)
print(cnt)