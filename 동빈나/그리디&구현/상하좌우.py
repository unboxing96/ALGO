import time
import sys
sys.stdin = open("상하좌우.txt", "r")

# 시작
start_time = time.time()

n = int(input())
directions = list(input().split())
current_idx = [1, 1]

operation_dict = {
    "R" : (0, 1),
    "L" : (0, -1),
    "U" : (-1, 0),
    "D" : (1, 0)
}

for current_operation in directions:
    row, col = operation_dict[current_operation]

    if 1 <= current_idx[0] + row <= 100 and 1 <= current_idx[1] + col <= 100:
        current_idx[0] += row
        current_idx[1] += col

print(current_idx)

end_time = time.time()
print(end_time - start_time)