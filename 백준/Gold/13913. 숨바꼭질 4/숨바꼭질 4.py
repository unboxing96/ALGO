from collections import deque

n, k = map(int, input().split())
INF = 100001
visited = [0] * INF
path = [0] * INF


def move(x):
    arr = []
    temp = x
    for _ in range(visited[x]):
        arr.append(temp)
        temp = path[temp]
    print(" ".join(map(str, arr[::-1])))


def bfs(n, k):
    visited[n] = 1
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(visited[x] - 1)
            move(k)
            return

        for nx in [x + 1, x - 1, 2 * x]:
            if 0 <= nx < INF:
                if not visited[nx] or visited[nx] >= visited[x] + 1:
                    q.append(nx)
                    visited[nx] = visited[x] + 1
                    path[nx] = x


bfs(n, k)
