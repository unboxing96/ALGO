from copy import deepcopy

def rotate(matrix, degree):
    def rotate_90(matrix):
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                rotated[y][n - x - 1] = matrix[x][y]
        return rotated

    time = (degree // 90) % 4
    rotated = deepcopy(matrix)
    for _ in range(time):
        rotated = rotate_90(rotated)
    return rotated

# TestCase 개수
T = int(input())

# TestCase만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    rotated90 = rotate(matrix, 90)
    rotated180 = rotate(matrix, 180)
    rotated270 = rotate(matrix, 270)

    print(f"#{tc}")
    for line in zip(rotated90, rotated180, rotated270):
        for row in line:
            print(*row, sep="", end=" ")
        print()