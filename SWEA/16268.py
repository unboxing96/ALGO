import sys
sys.stdin = open("16268.txt")

TC = int(input())

for tc in range(1, TC + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, 1, -1]
    max_tot = 0

    for x in range(n):
        for y in range(m):
            tmp_tot = 0
            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    tmp_tot += matrix[nx][ny]
            max_tot = max(max_tot, tmp_tot)
    
    print(f'#{tc} {max_tot}')
