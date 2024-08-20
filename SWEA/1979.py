import sys
sys.stdin = open("1979.txt")

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        h_tmp = 0
        v_tmp = 0
        for j in range(n):
            if matrix[i][j] == 1:
                h_tmp += 1
            else:
                if h_tmp == k:
                    result += 1
                h_tmp = 0

            if matrix[j][i] == 1:
                v_tmp += 1
            else:
                if v_tmp == k:
                    result += 1
                v_tmp = 0

        if h_tmp == k:
            result += 1

        if v_tmp == k:
            result += 1
    
    
    print(f'#{tc} {result}')