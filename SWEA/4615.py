import sys
sys.stdin = open("4615.txt")

# 문제 분석
# 가, 세, 정대, 역대 뒤집기

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [[0] * n for _ in range(n)]
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, -1, -1, 1, 1, -1]

    matrix[n // 2 - 1][n // 2 - 1] = 2
    matrix[n // 2 - 1][n // 2] = 1
    matrix[n // 2][n // 2 - 1] = 1
    matrix[n // 2][n // 2] = 2

    for _ in range(m):
        y, x, color = map(int, input().split())
        y -= 1
        x -= 1
        matrix[x][y] = color

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            path = []
            while 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] != 0:
                if matrix[nx][ny] != color:
                    path.append((nx, ny))
                    nx += dx[i]
                    ny += dy[i]
                else: # 다른 색상을 만났을 때만 뒤집기
                    for px, py in path:
                        matrix[px][py] = color
                    break
            
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                black += 1
            elif matrix[i][j] == 2:
                white += 1
    
    print(f'#{tc} {black} {white}')