n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def backTracking(idx, current_sum):
    global cnt

    if idx == n:
        if current_sum == s:
            cnt += 1
        return

    backTracking(idx + 1, current_sum + arr[idx])
    backTracking(idx + 1, current_sum)

backTracking(0, 0)

if s == 0:
    cnt -= 1

print(cnt)