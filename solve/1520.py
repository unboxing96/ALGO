import sys
sys.stdin = open("1520.txt", "r")

# 이해
# 경로의 개수?
# 1. DFS 백트래킹
# 2. DP

# 접근
# visited 2차원 배열 생성
# 내리막길로만 이동
# 현재 위치가 m-1, n-1이라면, return 1
# 아니라면 return 0

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dp = [[-1] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if x == r - 1 and y == c - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))