n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
cnt = 0

def check(tot, used):
    global cnt

    if tot < 0:  # 항상 중량이 0 이상인지 확인
        return

    if len(used) == n:  # 모든 운동 키트를 사용한 경우
        cnt += 1
        return

    for i in range(n):
        if i not in used and tot + nums[i] - k >= 0:
            used.append(i)
            check(tot + nums[i] - k, used)
            used.pop()

check(0, [])
print(cnt)
