# min -> start, max -> end 구함
# 이진탐색 진행.
# 탐색할 때마다 배열 전체를 탐색하면서 계산해도 O(N)
# 이진 탐색이 O(logN)번 진행될테니, 총 O(NlogN).

import sys
sys.stdin = open("떡볶이떡만들기.txt", "r")

n, m = map(int, input().split())
heights = list(map(int, input().split()))
result = 0

start = 0
end = max(heights)

while start <= end:
    
    total = 0
    mid = (start + end) // 2

    for hei in heights:
        if hei > mid:
            total += hei - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)