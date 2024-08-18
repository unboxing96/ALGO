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