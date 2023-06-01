
n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = []
cnt = 0

def check(start):
    global cnt

    if sum(ans) == s and len(ans) > 0:
        cnt += 1

    for i in range(start, n):
        ans.append(nums[i])
        check(i + 1)
        ans.pop()

check(0)
print(cnt)