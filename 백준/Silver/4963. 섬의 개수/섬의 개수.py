from collections import deque

# # DFS
# def dfs(x, y):
    
#     # 델타 이동
#     dx = [1, 1, -1, -1, 0, 0, 1, -1]
#     dy = [0, -1, 1, 0, 1, -1, 1, -1]

#     graph[x][y] = 0

#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
#             dfs(nx, ny)

# BFS
def bfs(x, y):

    # 델타 이동
    dx = [1, 1, -1, -1, 0, 0, 1, -1]
    dy = [0, -1, 1, 0, 1, -1, 1, -1]

    graph[x][y] = 0

    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])

while True:
    # 너비 x 높이
    w, h = map(int, input().split())

    # 0, 0 받으면 종료
    if w == 0 and h == 0:
        break
    
    cnt = 0

    graph = []
    # 높이 만큼 반복
    for _  in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
