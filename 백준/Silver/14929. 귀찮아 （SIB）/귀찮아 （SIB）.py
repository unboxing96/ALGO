n = int(input())
nums = list(map(int, input().split()))

prefix = 0
ans = 0

for i in range(n - 1):
    prefix += nums[i]
    ans += nums[i + 1] * prefix

print(ans)