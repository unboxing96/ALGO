from collections import deque

def bfs(start, end, maps):
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([start])
    dist = [[-1]*len(maps[0]) for _ in range(len(maps))]
    dist[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or maps[nx][ny] == 'X':
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist[end[0]][end[1]]

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    to_lever = bfs(start, lever, maps)
    to_end = bfs(lever, end, maps)
    if to_lever == -1 or to_end == -1:
        return -1
    return to_lever + to_end
