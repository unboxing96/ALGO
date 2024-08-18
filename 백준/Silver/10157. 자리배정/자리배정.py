
y, x = map(int, input().split())
k = int(input())

if k > x * y:
    print(0)

else:
    matrix = [[0] * y for _ in range(x)]
    cx = x - 1
    cy = 0
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d_pointer = 0

    matrix[cx][cy] = 1

    for num in range(2, k + 1):
        nx = cx + dir[d_pointer % 4][0]
        ny = cy + dir[d_pointer % 4][1]

        if nx < 0 or nx >= x or ny < 0 or ny >= y or matrix[nx][ny] != 0:
            d_pointer += 1
            nx = cx + dir[d_pointer % 4][0]
            ny = cy + dir[d_pointer % 4][1]
        
        matrix[nx][ny] = num

        cx = nx
        cy = ny
    
    print(cy + 1, x - 1 - cx + 1)
