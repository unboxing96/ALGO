from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []


def bfs():
    # 시작점
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny]:
                # 0에서 0으로
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))  # 항상 0만 q에 append
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = 0  # melt when aside with air
                    cnt += 1
    ans.append(cnt)
    return cnt


time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    if not bfs():
        break
    time += 1

print(time)
print(ans[-2])
