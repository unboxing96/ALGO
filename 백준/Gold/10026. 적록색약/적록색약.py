import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 방문한 문자 저장
    now = graph[x][y]

    # 방문 처리
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            continue

        if graph[nx][ny] == now:
            dfs(nx, ny)


def new_dfs(x, y):
    # 방문한 문자 저장
    now = new_graph[x][y]

    # 방문 처리
    new_graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if new_graph[nx][ny] == 0:
            continue

        if new_graph[nx][ny] == now:
            new_dfs(nx, ny)


n = int(input())

graph = []
new_graph = []
for _ in range(n):
    temp = input()
    graph.append(list(temp))
    new_graph.append(list(temp.replace("R", "G")))

result = 0
new_result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            dfs(i, j)
            result += 1

        if new_graph[i][j] != 0:
            new_dfs(i, j)
            new_result += 1

print(result, new_result)