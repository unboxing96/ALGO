import sys
sys.stdin = open("16236.txt")

# 문제 분석
# 아기 상어 크기 2
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기 선택
# 같은 거리 물고기가 여러 마리 -> 가장 위쪽 -> 가장 왼쪽
# 상어는 자기 크기만큼 물고기를 먹으면, 크기가 1 증가한다.

# 접근
# def find_closest_fish()
# 매번 행렬을 전체 탐색하여, 현재 크기보다 작은 물고기들의 위치를 tmp 배열에 담는다. (x, y)
    # 배열을 x와 y의 오름차순으로 정렬한다.
    # 해당 배열을 모두 탐색하여, 거리가 가장 가까운 물고기를 찾는다. BFS를 이용한다.
        # 정렬된 베열이므로, 언제나 가장 위쪽, 왼쪽에 위치한 물고기가 후보가 된다.

# find_closest_fish()가 물고기를 찾지 못 할 때까지 반복한다.
# 찾은 물고기 좌표로 이동한다.
    # 거리만큼 time에 더한다.
    # 상어 경험치가 1 증가한다.
        # 경험치를 꽉 채우면 크기가 1 증가한다. 경험치는 다시 0으로 초기화 된다.
    # 기존 상어 위치는 0으로 갱신한다.

from collections import deque
import copy

def get_distance(sx, sy, tx, ty): # 상어 위치 / 목표 위치
    q = deque()
    q.append((sx, sy, 0))
    new_matrix = copy.deepcopy(matrix)
    new_matrix[sx][sy] = -1

    while q:
        x, y, time = q.popleft()
        # print("x, y, time", x, y, time)

        if x == tx and y == ty:
            return time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and new_matrix[nx][ny] <= shark_size and new_matrix[nx][ny] != -1:
                new_matrix[nx][ny] = -1
                q.append((nx, ny, time + 1))
    
    return 0

def find_closest_fish(sx, sy):
    tmp = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and matrix[i][j] != 9:
                tmp.append((i, j))
    
    tmp.sort(key = lambda x : (x[0], x[1]))

    min_dist = 401
    min_loc = [-1, -1]

    for tx, ty in tmp:
        if matrix[tx][ty] >= shark_size:
            continue
        # print("tx, ty", tx, ty)
        tmp_dist = get_distance(sx, sy, tx, ty)
        # print("tmp_dist: ", tmp_dist)
        if tmp_dist < min_dist:
            min_dist = tmp_dist
            min_loc = [tx, ty]
    
    if min_dist == 401:
        return [0, 0, 0]
    else:
        return [min_dist, min_loc[0], min_loc[1]]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
shark_size = 2
shark_exp = 0
sx = 0
sy = 0
result = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            sx = i
            sy = j

while True:
    dist, next_fish_x, next_fish_y = find_closest_fish(sx, sy)
    # print(dist, next_fish_x, next_fish_y)
    if dist:
        matrix[sx][sy] = 0
        sx = next_fish_x
        sy = next_fish_y
        matrix[sx][sy] = 9

        shark_exp += 1
        if shark_exp == shark_size:
            shark_size += 1
            shark_exp = 0
        
        result += dist
    
    else:
        break

print(result)