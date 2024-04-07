# 14:15

# 이해
# 복잡한 도형의 둘레를 따라서만 이동이 가능하다.
# 시작 좌표와, 도착 좌표가 주어진다. 도착할 때까지 최소 거리는? BFS.
# 좌표 개념이 배열과 반대이다. 현실 세계의 그것과 같다.

# 풀이
# 51 x 51 행렬을 만들고 0으로 초기화 한다.
# rectangle을 탐색하면서, range(rec[0], rec[2] + 1): range(rec[1], rec[3] + 1): 범위의 테두리를 1로 만든다.
# BFS 탐색을 한다.
    # 큐를 생성하고 시작 노드를 큐에 넣는다.
    # 큐를 반복한다.
    # 원소를 pop한다.
    # pop한 원소가 itemX, itemY와 같다면, return 한다.
    # 4방향 탐색을 한다.
    # nx, ny를 구한다.
    # 범위를 벗어나면 continue 한다.
    # 0을 만나면 continue 한다.
    # 1보다 큰 값을 만나면 continue 한다.
    # nx, ny 위치에서 4방향 탐색을 한번 더 한다.
        # 여기서 4방향 중 하나라도 0을 만나야 한다. (그래야 테두리)
        # 못 만나면 바깥 루프 기준 conitnue
    # [nx][ny] = [x][y] + 1
    # 큐에 (nx, ny) 추가

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    graph = [[-1 for i in range(102)] for _ in range(102)]
    visited = [[0 for i in range(102)] for _ in range(102)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1 # 테두리는 1, 내부는 0, 외부는 -1
    
    
    answer = bfs(cx, cy, ix, iy, graph, visited, dx, dy)
    return answer
    
    
def bfs(characterX, characterY, itemX, itemY, graph, visited, dx, dy):
    
    q = deque([(characterX, characterY)])
    
    while q:
        (x, y) = q.popleft()
        
        if x == itemX and y == itemY:
            return visited[itemX][itemY] // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 1 or nx >= 102 or ny < 1 or ny >= 102: # 범위를 벗어남.
                continue
            
            if visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return -1
                






