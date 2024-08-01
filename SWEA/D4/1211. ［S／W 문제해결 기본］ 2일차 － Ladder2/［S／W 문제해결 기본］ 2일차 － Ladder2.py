# 문제 분석
# 바닥까지 가장 짧은 거리를 갖는 시작점의 x 좌표 (코드 상으로 y 좌표) return
# 여러 개인 경우 가장 큰 x 좌표(코드 상으로 y 좌표)를 반환

# 접근
# move 함수의 탈출 조건을 matrix[cur_x][cur_y] == 1으로 하자. return cur_y
    # 바닥에 도달할 때까지 탈출하지 못 하면 return - 1
# main 함수에서 -1이 아닌 값을 return 받을 때마다, 반환할 시작점의 좌표를 업데이트 한다.
# 애초에 정방향 탐색으로 move 함수를 실행하면, 자동으로 가장 큰 시작점 좌표가 저장될 것이다.

def change_direction(d, x, y):
    directions = direction_interchange[d]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 100 and 0 <= ny < 100 and matrix[nx][ny] == 1:
            return (dx, dy)
    return d

def move(d, cur_x, cur_y, cnt):
    while cur_x < 100:
        if cur_x == 100 - 1 and matrix[cur_x][cur_y] == 1:
            return cnt

        d = change_direction(d, cur_x, cur_y)
        cur_x += d[0]
        cur_y += d[1]
        cnt += 1

    return -1

direction_interchange = {
    (1, 0) : [(0, 1), (0, -1)],
    (0, 1) : [(1, 0)],
    (0, -1) : [(1, 0)]
}

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result_cnt = 10001
    result_index = -1

    for i in range(100):
        if matrix[0][i] == 1:
            cnt = move((1, 0), 0, i, 1)
            if cnt != -1:
                if result_cnt > cnt:
                    result_cnt = cnt
                    result_index = i

    print(f'#{tc} {result_index}')



