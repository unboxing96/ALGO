import sys
sys.stdin = open("14503.txt")

# 문제 분석
# 현재 칸이 0인 경우 청소
# 방문 가능한 곳이 있는 경우
    # 반시계 90도 회전
    # 현재 방향 기준 앞쪽 칸이 빈 칸인 경우 전진
# 없는 경우
    # 후진
    # 더 이상 갈 곳이 없는 경우 종료

# 접근

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
