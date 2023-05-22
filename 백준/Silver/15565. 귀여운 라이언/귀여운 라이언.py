
n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = int(1e9)
cnt = 0 # 현재 투 포인터에서 라이언 수
i = 0
j = 0

if nums[j] == 1:
    cnt += 1

while j < n:
    if cnt == k:
        
        ans = min(ans, j - i + 1)
        
        if nums[i] == 1:
            cnt -= 1

        i += 1
    
    else:
        j += 1
        if j < n and nums[j] == 1:
            cnt += 1

if ans == int(1e9):
    print(-1)
else:
    print(ans)