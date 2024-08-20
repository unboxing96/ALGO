import sys
sys.stdin = open("2116.txt")

# 문제 분석
# 방향 하나만 정하면 나머지는 자동이다.
# 6 * 10,000 이라는 뜻이다.
# 주사위 반대편의 인덱스를 구하는 함수 get_opposite_index()
# 첫 번째 주사위에서 시작 인덱스를 정한다.
# 함수로 반대 인덱스를 구한다.
# [1, 2, 3, 4, 5, 6]에서 시작 인덱스와 반대 인덱스 위치의 값을 뺀 값 중 최대값을 tot에 더한다.
# 6개의 값에 대하여 n번 반복한다.
# 이 중에서 최대값을 return 한다.

def get_opposite_index(start):
    if start == 1:
        return 6
    elif start == 2:
        return 4
    elif start == 3:
        return 5
    elif start == 4:
        return 2
    elif start == 5:
        return 3
    else:
        return 1

n = int(input())
dices = [[0] + list(map(int, input().split())) for _ in range(n)]
tot = 0

for start_index in range(1, 6 + 1):
    tmp_tot = 0
    for i in range(n):
        dice_value_arr = [1, 2, 3, 4, 5, 6]
        opposite_index = get_opposite_index(start_index)
        dice_value_arr.remove(dices[i][start_index])
        dice_value_arr.remove(dices[i][opposite_index])

        tmp_tot += max(dice_value_arr)

        if i + 1 < n:
            start_index = dices[i + 1].index(dices[i][opposite_index])
    
    tot = max(tot, tmp_tot)

print(tot)
    