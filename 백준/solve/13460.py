from pprint import pprint
import sys

sys.stdin = open("13460.txt", "r")

#####
# 4방 탐색
# 해당 방향 끝까지 굴러감
# 0은 이동 중에 만나도 ㄱㅊ
# B가 먼저 혹은 동시에 0을 만나면 안 됨
# 이동 횟수 10 넘어가면 종료
# 이동 횟수 출력

from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            R_idx = [i, j]
        if graph[i][j] == "B":
            B_idx = [i, j]
        if graph[i][j] == "O":
            goal = [i, j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q1 = deque()
    q2 = deque()
    q1.append(R_idx)
    q2.append(B_idx)

    while q1 and q2:
        x1, y1 = q1.popleft()
        x2, y2 = q2.popleft()

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[1]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[1]

            while True:
                if graph[nx1][ny1] == "#" or graph[nx1][ny1] == "B":
                    
