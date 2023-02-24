
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                cnt += 1
                dfs(nx, ny)


cnt_list = []
time = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i, j)
            cnt_list.append(cnt)
            time += 1

cnt_list.sort()

print(time)
print(*cnt_list, sep="\n")
