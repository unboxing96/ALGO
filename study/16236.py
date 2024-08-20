import sys
sys.stdin = open("16236.txt")

# 문제 분석
# 상어는 4방 탐색한다.
# 상어는 자기보다 큰 물고기를 지나갈 수 없다.
# 상어는 자기와 같은 물고기를 지나갈 수 있다.
# 상어는 자기보다 작은 물고기를 먹을 수 있다.

# 전체 행렬 내에 더 이상 '먹을 수 있는' 물고기가 없다면 종료한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, '거리가 가까운' 물고기를 먹으러 간다.
    # 거리: 이동해야 하는 칸의 개수의 최솟값
# 거리가 동일하게 가까운 물고기가 많다면, 위쪽에 있는 물고기
    # 그런 물고기가 많다면, 왼쪽에 있는 물고기

# 물고기를 먹을 수 있는 경우, 먹고, 그 칸은 빈 칸이 된다.
# 자기 몸무게 만큼 물고기를 먹으면 크기가 += 1

# 접근
# 이동은 4방이다.
# 탐색은 그보다 많이 할 수 있다. 즉, 미리 탐색하여 먹을 물고기를 정하고 이동한다.
    # 이때 우선순위는 거리 -> 위쪽 -> 왼쪽 순서로 적용한다.
        # XXXX 거리는 abs(x2 - x1) + abs(y2 - y1)
            # 아니다. 장애물이 있으므로 BFS 탐색으로 최소 이동 거리를 구한다.
        # 같은 목표 인덱스에서는, x가 작은 값 -> y가 작은 값으로 정렬하여 선택한다.
# 정했으면 이동해서 먹는다.
    # 먹었으면 to_next_level += 1
    # to_next_level가 상어 크기만큼 되면, 상어 크기 += 1, to_next_level = 0
    # 상어의 무게는 weight 변수로 따로 관리하는 것이 편하겠다.
# 이동마다 time += 1
# 더 이상 먹을 수 없으면 return time


from collections import deque

def get_closest_fish_candidates(i, j): # candidate_fish_arr, arrive_time
    q = deque()
    q.append([i, j, 0])
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1 # 시작 위치 방문 처리

    while q:
        x, y, time = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] <= weight and not visited[nx][ny]:
                if matrix[nx][ny] < weight:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1))
    
    

    candidates_arr = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 9 and matrix[i][j] != 0:
                candidates_arr.append(i, j, matrix[i][j])
    
    return candidates_arr



n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
fish_arr = []
shark_x = 0
shark_y = 0
weight = 2
to_next_level = 0
time = 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            shark_x = i
            shark_y = j
        elif matrix[i][j] != 0:
            fish_arr.append((i, j, matrix[i][j])) # x, y, size

while True:
    candidate_fish_arr = get_closest_fish_candidates(shark_x, shark_y)
    print(candidate_fish_arr)
    candidate_fish_arr.sort(key = lambda x : (x[1], x[0]))

    if candidate_fish_arr: # 먹을 수 있는 물고기가 있으면
        closest_fish = candidate_fish_arr[0]
        (nx, ny, arrive_time) = closest_fish

        matrix[shark_x][shark_y] = 0
        shark_x = nx # 이동
        shark_y = ny
        matrix[nx][ny] = 9 # 이동
        time += arrive_time # 이동하는 시간

        to_next_level += 1
        if to_next_level == weight:
            weight += 1
            to_next_level = 0
        
        continue

    else:
        break # 더 이상 먹을 수 있는 물고기가 없다면 종료

    time += 1