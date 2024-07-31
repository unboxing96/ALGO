# TestCase 개수
T = int(input())

# TestCase만큼 반복
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_tmp = -1e9

    for i in range(N - (M - 1)):
        for j in range(N - (M - 1)):
            tmp = 0
            for ni in range(i, i + M):
                for nj in range(j, j + M):
                    tmp += matrix[ni][nj]

            if max_tmp < tmp:
                max_tmp = tmp

    print(f'#{tc} {max_tmp}')
