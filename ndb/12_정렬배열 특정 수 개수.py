from bisect import bisect
import collections
import sys
sys.stdin = open("12_정렬배열 특정 수 개수.txt", "r")

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

result = bisect_right(array, 2) -  bisect_left(array, 2)
print(result)