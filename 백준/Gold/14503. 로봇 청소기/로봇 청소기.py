n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def move(x, y, d):
    global cnt
    if matrix[x][y] == 0:
        matrix[x][y] = 2  # 청소한 칸은 2로 표시
        cnt += 1
    
    for _ in range(4):
        d = (d - 1) % 4  # 반시계 방향으로 회전
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
            return nx, ny, d, True
    
    # 네 방향 모두 청소가 되어 있거나 벽인 경우
    nx = x - dx[d]
    ny = y - dy[d]
    if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 1:
        return nx, ny, d, True  # 후진
    else:
        return x, y, d, False  # 종료 조건

while True:
    r, c, d, can_move = move(r, c, d)
    if not can_move:
        print(cnt)
        break
