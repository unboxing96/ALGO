def count_candy():
    row_cnt = 1
    col_cnt = 1
    row_max = -1e9
    col_max = -1e9

    for i in range(n):
        for j in range(n - 1):
            if data[i][j] == data[i][j + 1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    for j in range(n):
        for i in range(n - 1):
            if data[i][j] == data[i + 1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_max, col_cnt)
        col_cnt = 1

    answer = max(row_max, col_max)
    return answer


ans = 0
n = int(input())
data = [list(input()) for _ in range(n)]
steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + steps[k][0]
            ny = j + steps[k][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if data[i][j] != data[nx][ny]:
                data[nx][ny], data[i][j] = data[i][j], data[nx][ny]
                ans = max(ans, count_candy())
                data[nx][ny], data[i][j] = data[i][j], data[nx][ny]

print(ans)
