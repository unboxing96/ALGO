# w, h 매트릭스 생성
# 매트릭스 1번 탐색하며, 한 층씩 visited 처리
# 매트릭스 다시 1번 탐색하며, 0을 만나면, 해당 층을 탐색하며, 양쪽에 1이 있으면 cnt += 1

h, w = map(int, input().split())
waters = list(map(int, input().split()))

ans = 0
for i in range(1, w-1):
    left = max(waters[:i])
    right = max(waters[i+1:])
    compare = min(left, right)
    if waters[i] < compare:
        ans += compare- waters[i]
        
print(ans)