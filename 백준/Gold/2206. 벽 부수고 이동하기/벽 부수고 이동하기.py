from collections import deque

n, m = map(int, input().split()) # 실제로는 -1 해서 사용
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # visited[x][y][0]은 벽 파괴 가능, visited[x][y][1]은 벽 파괴 불가능
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0, 0)) # x, y, is_break_done
    visited[0][0][0] = 1

    while q:
        x, y, c = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 아직 벽 파괴 기회가 남아있는 경우 -> 파괴 !
            if matrix[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[x][y][c] + 1
                q.append((nx, ny, 1))

            # 다음 이동할 곳이 벽이 아니고, 방문하지 않은 경우
            elif matrix[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                q.append((nx, ny, c))
    
    return -1

print(bfs())