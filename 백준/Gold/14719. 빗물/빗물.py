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