n = int(input())
nums = list(map(int, input().split()))
nums.sort()

tot = 0
for i in range(len(nums)):
    tot += nums[i] * (n - i)

print(tot)
