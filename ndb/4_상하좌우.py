# 2차원 매트릭스 구현 range(N):

# R = [0, 1]
# U = [-1, 0]
# L = [0, -1]
# D = [1, 0]

# 반복하며 입력값을 받아, 정해진 델타만큼 이동
# 행, 열이 1보다 작으면 pass

from pprint import pprint


N = int(input())
plans = input().split()

x, y = 1, 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
command = ["D", "U", "R", "L"]

for plan in plans:
    for i in range(len(command)):
        if command[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    else:
        x = nx
        y = ny

print(x, y)

