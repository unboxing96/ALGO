n, s = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] <= s:
            cnt += 1
        else:
            break

print(cnt)