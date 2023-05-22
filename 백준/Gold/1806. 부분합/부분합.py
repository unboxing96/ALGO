n, s = map(int, input().split())
nums = list(map(int, input().split()))
prefix = nums[0]
ans = 100001
start = 0
end = 0

while True:
    if prefix >= s:
        prefix -= nums[start]
        ans = min(ans, end - start + 1)
        start += 1
    else:
        end += 1
        if end == n:
            break
        prefix += nums[end]

if ans == 100001:
    print(0)
else:
    print(ans)