
n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
start = 0
end = 0

while start < n:

    if end == n:
        break

    if sum(nums[start : end + 1]) == m:
        cnt += 1
        start += 1

    elif sum(nums[start : end + 1]) > m:
        start += 1
        
    else:
        end += 1

print(cnt)