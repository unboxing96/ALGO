import sys

sys.stdin = open("2309.txt", "r")

height_list = []

for _ in range(9):
    height_list.append(int(input()))

height_list.sort()

sum_ = sum(height_list)

for i in range(len(height_list)):
    for j in range(1, len(height_list)):
        if sum_ - height_list[i] - height_list[j] == 100:
            a = height_list[i]
            b = height_list[j]

for height in height_list:
    if height == a or height == b:
        pass
    else:
        print(height)
