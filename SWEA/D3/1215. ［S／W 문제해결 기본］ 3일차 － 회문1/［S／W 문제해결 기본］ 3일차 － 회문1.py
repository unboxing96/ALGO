# TestCase 개수
T = 10

# TestCase만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(input()) for _ in range(8)]
    result = 0

    for i in range(8):
        for j in range(8 - n + 1):
            substring = matrix[i][j : j + n]
            if substring == substring[::-1]:
                result += 1

    for j in range(8):
        for i in range(8 - n + 1):
            substring = "".join([matrix[i + k][j] for k in range(n)])
            if substring == substring[::-1]:
                result += 1

    print(f'#{tc} {result}')