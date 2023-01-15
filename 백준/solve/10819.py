import sys

sys.stdin = open("10819.txt", "r")

from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

perm = list(permutations(nums, n))

result = []
for p in perm:
    tot = 0
    for i in range(1, n):
        tot += abs(p[i] - p[i - 1])
    result.append(tot)

print(max(result))
