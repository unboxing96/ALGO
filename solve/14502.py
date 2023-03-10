from pprint import pprint
import sys
sys.stdin = open("14502.txt", "r")

# 벽을 세울 위치를 조합으로 구해 완탐
# bfs로 바이러스 모두 퍼지게 함
# 전체 그래프 탐색하며 0 개수 세기

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    g = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == 0:
                    g[nx][ny] = 2
                    q.append((nx, ny))
    
    global answer
    
    cnt = 0
    for i in range(n):
        cnt += g[i].count(0)
    
    answer = max(answer, cnt)



def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt  + 1)
                graph[i][j] = 0

answer = 0
make_wall(0)
print(answer)

