T = int(input())

for i in range(T):

    M, N = map(int, input().split()) # M = 5, N = 4
    sum_ = 0

    # 매트릭스 생성
    matrix = []
    for i in range(M):
        matrix.append(list(map(int, input().split())))


# 열 * 행 만들기
    for n in range(N): # 열: 4

        cnt = 0
        for m in range(M): # 행: 5

            if matrix[m][n] == 1:
                sum_ += (M - 1) - m - cnt
                cnt += 1

    print(sum_)
