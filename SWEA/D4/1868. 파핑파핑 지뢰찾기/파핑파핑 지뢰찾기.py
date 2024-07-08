from collections import deque

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [1, -1, 1, -1, 0, 0, 1, -1]

def openMatrix(x, y):
    tmp = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if matrix[nx][ny] == "*":
            tmp += 1
    
    matrix[x][y] = tmp


def clickZeroElement(a, b):

    q = deque()
    q.append([a, b])
    matrix[a][b] = "*"

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if matrix[nx][ny] == 0:
                q.append([nx, ny])
                matrix[nx][ny] = "*"
            
            elif matrix[nx][ny] != "*":
                matrix[nx][ny] = "*"

testCase = int(input())

for tc in range(testCase):
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == ".":
                openMatrix(i, j)
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                clickZeroElement(i, j)
                total += 1
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != "*":
                total += 1
    
    print(f"#{tc + 1} {total}")