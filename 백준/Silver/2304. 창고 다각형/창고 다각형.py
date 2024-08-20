n = int(input())
arr = []
top_height = 0
top_idx = 0
tot = 0

for _ in range(n):
    idx, height = map(int, input().split())
    if top_height < height:
        top_height = height
        top_idx = idx
    arr.append((idx, height))

tot += top_height
arr.sort()

left_max_height = arr[0][1]
right_max_height = arr[-1][1]
left_pivot = 0
right_pivot = len(arr) - 1

for i in range(arr[0][0], top_idx):
    if i == arr[left_pivot][0]:
        if left_max_height < arr[left_pivot][1]:
            left_max_height = arr[left_pivot][1]
        left_pivot += 1
    tot += left_max_height

for i in range(arr[-1][0], top_idx, -1):
    if i == arr[right_pivot][0]:
        if right_max_height < arr[right_pivot][1]:
            right_max_height = arr[right_pivot][1]
        right_pivot -= 1
    tot += right_max_height

print(tot)