# 이해
# 최단 경로 BFS
# 도착할 수 없는 경우 -1 return

# 풀이
# BFS로 풀이한다.
# 누적 거리에 대한 정보를 maps에 그대로 덮어써도 무방하겠다.
# 더 이상 이동할 곳이 없는 경우 즉시 -1을 return 한다.
# n - 1, m - 1 위치에 도달한 경우 해당 위치의 값을 return 한다.

from collections import deque

def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    return bfs(maps, visited)

def bfs(maps, visited):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(0, 0)])
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if not visited[nx][ny] and maps[nx][ny] != 0:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return -1
        
        
        
        
        
        
        