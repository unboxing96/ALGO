# 이해
# 최소 거리 문제 -> BFS
# 도착할 수 없을 경우 -> -1
# 정사각형 형태 아님

# 풀이
# maps의 0,0 위치에서 bfs()
# if maps[n-1][m-1] != 1: 값 return else -1 return

# bfs()
# 큐 생성 후 첫 번째 노드 추가
# 큐 반복
    # x == n-1 and y == m-1이라면
        # return maps[n-1][m-1]
    # 4방향을 탐색하며, 범위를 벗어나지 않고, 방문하지 않고, 1인 경우
        # 이전 값을 다음 위치에 추가 (방문 처리와 같다.)
        # 큐에 추가

from collections import deque
        
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    answer = bfs(0, 0, n, m, dx, dy, maps)
    return -1 if answer == 1 else answer

def bfs(x, y, n, m, dx, dy, maps):
    q = deque([(x, y)])
    
    while q:
        (x, y) = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return maps[n-1][m-1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 벗어남
                continue
                
            if maps[nx][ny] == 0: # 벽돌
                continue
            
            if maps[nx][ny] > 1: # 방문했던 곳
                continue
            
            maps[nx][ny] = maps[x][y] + 1 # 방문 처리, 거리 계산
            q.append((nx, ny))
    
    return 1
    
    
    
    
    
    
    