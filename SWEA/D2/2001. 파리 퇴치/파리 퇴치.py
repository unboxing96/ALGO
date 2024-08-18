
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_tmp = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            tmp = 0
            for mi in range(m):
                for mj in range(m):
                    tmp += matrix[i + mi][j + mj]
            max_tmp = max(max_tmp, tmp)
    
    print(f"#{tc} {max_tmp}")
            