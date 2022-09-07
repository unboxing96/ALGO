from time import time
import sys
sys.stdin = open("11_떡볶이 떡 만들기.txt", "r")

start_time = time()

n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = max(nums)

result = 0
while start <= end:
  tot = 0
  mid = (start + end) // 2
  for x in nums:
    if x > mid:
      tot += x - mid
  
  if tot < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)







end_time = time()

print(end_time - start_time)