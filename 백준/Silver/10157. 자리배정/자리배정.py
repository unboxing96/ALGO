C, R = map(int, input().split())  # 공연장 좌석 크기 입력 (가로 C, 세로 R)
K = int(input())  # 대기번호 입력

if K > C * R:
    print(0)
else:
    matrix = [[0] * C for _ in range(R)]  # 행렬 초기화
    cx = R - 1  # 현재 x좌표 (행)
    cy = 0      # 현재 y좌표 (열)
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 방향 설정 (위, 오른쪽, 아래, 왼쪽)
    d_pointer = 0  # 현재 방향

    matrix[cx][cy] = 1  # 첫 번째 관객 배정

    for num in range(2, K + 1):
        nx = cx + dir[d_pointer % 4][0]
        ny = cy + dir[d_pointer % 4][1]

        # 범위를 벗어나거나 이미 채워진 경우 방향 전환
        if nx < 0 or nx >= R or ny < 0 or ny >= C or matrix[nx][ny] != 0:
            d_pointer += 1
            nx = cx + dir[d_pointer % 4][0]
            ny = cy + dir[d_pointer % 4][1]

        matrix[nx][ny] = num

        cx = nx
        cy = ny

    # 결과 출력
    print(cy + 1, R - cx)
