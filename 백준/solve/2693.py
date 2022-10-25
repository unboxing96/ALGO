tc = int(input())

for _ in range(tc):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])