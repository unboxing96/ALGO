
# 문제 분석
# 사다리타기를 구현한다.
# 내려가는 방향(1, 0)일 때는 (0, -1), (0, 1)만 살핀다.
    # 해당 위치에 값(1)이 있으면, 방향을 전환하여 이동한다.
# 가로로 이동하는 방향(0, -1), (0, 1)일 때는 (1, 0)만 살핀다.
    # # 해당 위치에 값(1)이 있으면, 방향을 전환하여 이동한다.


# 방향 전환이 가능한 위치인지 판단
def check_new_direction(d, matrix, x, y):
    directions = direction_interchange[d]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 100 and 0 <= ny < 100 and matrix[nx][ny] >= 1: # 1이거나 2를 찾으면 방향 전환
            return (dx, dy)
    return d


# 위치 이동
def move(d, cur_x, cur_y):
    while cur_x < 100:  # 99번째 줄까지 내려가면 종료
        if matrix[cur_x][cur_y] == 2:  # 목표 도착
            return cur_y  # 도착한 y좌표 반환

        d = check_new_direction(d, matrix, cur_x, cur_y)
        cur_x += d[0]
        cur_y += d[1]

    return -1  # 도착점에 도달하지 못한 경우


# 방향 전환을 위한 딕셔너리
direction_interchange = {
    (1, 0): [(0, -1), (0, 1)],  # 아래 -> 좌, 우
    (0, -1): [(1, 0)],  # 좌 -> 아래
    (0, 1): [(1, 0)]  # 우 -> 아래
}


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    result = -1
    for i in range(100):
        if matrix[0][i] == 1:  # 출발할 수 있는 경우
            if move((1, 0), 0, i) != -1:  # 도착점에 도달한 경우
                result = i # 출발 인덱스를 할당
                break

    print(f"#{tc} {result}")
