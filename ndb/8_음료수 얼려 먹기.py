

import sys
sys.stdin = open("8_음료수 얼려 먹기.txt", "r")

# 0으로 된 덩어리 개수 세기
# 매트릭스 전체 탐색
# 탐색 중 0을 만나면, DFS 탐색 (델타 탐색으로 진행: 상하좌우 인접해야 덩어리니까) 후 True
# 탐색 중 1을 만나면, False
# 탐색 중 매트릭스 범위를 벗어나면, False (<- 없어도 될 듯?)

# 매트릭스 생성
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 델타 좌표
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# dfs 함수 정의
def dfs(x, y):
    # print(x, y, "dfs 함수 내")
    if x <= -1 or x >= n or y <= -1 or y >= m:
        # print(x, y, "범위 초과")
        return False
    # 좌표에 방문하지 않았다면, 방문 처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        # dfs 탐색으로 인접 리스트 전부 방문 처러ㅣ
        for i in range(n):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

result = 0

# 매트릭스 전부 탐색
# True일 때 (덩어리 찾고, DFS 완료했을 떄), result += 1
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)