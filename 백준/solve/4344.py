import sys

sys.stdin = open("4344.txt", "r")

tc = int(input())

for _ in range(tc):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]

    cnt = 0
    for num in nums[1:]:
        if num > avg:
            cnt += 1

    result = cnt / nums[0] * 100
    print(f"{result: .3f}%")
1
