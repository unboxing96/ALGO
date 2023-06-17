k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

l = 1
r = max(k_list)

while l <= r:

    mid = (l + r) // 2
    tot = 0

    for i in range(k):
        tot += k_list[i] // mid
    
    if tot >= n:
        l = mid + 1
    
    else:
        r = mid - 1

print(r) 