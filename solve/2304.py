import sys
sys.stdin = open("2304.txt")

# 문제 분석
# 가장 높은 막대를 기준으로 left, right를 나눈다.
# 입력값을 위치를 기준으로 정렬한다.
# 각 파트의 최대값을 갱신해가며 전체 넓이에 더해준다.

# 접근
# left는 left 배열의 가장 앞에 위치한 막대를 기준으로 시작한다.
# tot = 0
# left_max_height = left[0][1]
# left_idx = left[0][0]
# for i in range(left_idx, top_idx):
    # if left_max_height < left[i][1]:
        # left_max_height = left[i][1]
    # tot += left_max_height
# right는 반대로 진행
# 마지막에 top_max_height를 더해준다.

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