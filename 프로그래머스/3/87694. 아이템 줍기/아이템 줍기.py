# 이해
# 여러 개의 다각형이 겹쳐져 있음
# 겹쳐진 지형의 테두리를 따라서만 이동이 가능
# 이때 특정 위치에서 특정 위치로 이동하는 최단 거리를 return

# 주의할 점
# 다각형이 겹치기 때문에, 의도치 않게 내부의 경로를 따라 움직일 가능성이 있다. -> 테두리는 1, 도형 안쪽은 -1로 채운다.
# 두 개의 변이 딱 붙어있다면, 의도치 않게 테두리를 따라 이동하지 않고, 가로지를 가능성이 있다. -> 그래프를 2배로 확장

# 풀이
# 최단 거리 -> BFS
# 51 * 2 크기의 그래프를 생성한다.
# rectangle 배열을 탐색하여 그래프를 채운다.
    # 주어진 좌표를 모두 2를 곱한다.
    # 테두리인 경우 1로 채운다.
    # 테두리가 아닌 경우 -1로 채운다.
# BFS를 진행한다.
    # characterX, characterY, itemX, itemY 모두 2배로 만든다.
    # 큐를 생성한다.
    # 큐에 cX, cY를 삽입한다.
    # 큐가 빌 때까지 반복한다.
        # 큐에서 노드를 꺼낸다.
        # 해당 노드가 iX, iY와 일치한다면 최단 거리를 return 한다.
    # 범위를 벗어나면 continue
    # nx, ny가 0 혹은 -1 이라면 continue
    # nx, ny가 1인 경우에만 진행
    # 방문 처리는 따로 필요 없지 않을까? 왜냐하면 nx, ny가 1인 경우 == 방문하지 않은 곳이기 때문에

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    
    for rec in rectangle:
        lx, ly, rx, ry = map(lambda x: x * 2, rec)
        
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                if x == lx or x == rx or y == ly or y == ry:
                    if graph[x][y] != -1:
                        graph[x][y] = 1
                else:
                    graph[x][y] = -1
    
    return bfs(characterX, characterY, itemX, itemY, graph)


def bfs(characterX, characterY, itemX, itemY, graph):
    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(cx, cy)])
    
    while q:
        x, y = q.popleft()
        
        if x == ix and y == iy:
            return graph[x][y] // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 102 or ny <= 0 or ny >= 102:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))









