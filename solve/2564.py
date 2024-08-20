import sys
sys.stdin = open("2564.txt")

# 문제 분석
# 걍 달팽이
# min(이동 거리, 전체 둘레 - 이동 거리)
# 행렬은 크기를 1씩 크게 하자.


# 블록의 가로와 세로 길이
width, height = map(int, input().split())
# 상점의 개수
n = int(input())

# 경계의 총 길이
perimeter = 2 * (width + height)

def get_perimeter_position(direction, distance):
    """
    주어진 방향과 거리로 경계선 상의 일차원 위치를 반환합니다.
    """
    if direction == 1:  # 북쪽
        return distance
    elif direction == 2:  # 남쪽
        return width + height + (width - distance)
    elif direction == 3:  # 서쪽
        return width + height + width + (height - distance)
    elif direction == 4:  # 동쪽
        return width + distance

# 상점 위치 저장
store_positions = []
for _ in range(n):
    dir, dist = map(int, input().split())
    store_positions.append(get_perimeter_position(dir, dist))

# 동근이의 위치 입력
dg_dir, dg_dist = map(int, input().split())
dg_position = get_perimeter_position(dg_dir, dg_dist)

# 최단 거리의 합 계산
total_distance = 0
for store_pos in store_positions:
    # 직선 거리
    direct_distance = abs(dg_position - store_pos)
    # 반대 방향 거리
    opposite_distance = perimeter - direct_distance
    # 최단 거리
    shortest_distance = min(direct_distance, opposite_distance)
    total_distance += shortest_distance

print(total_distance)

