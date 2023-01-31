
import sys

sys.setrecursionlimit(10**9)


def dfs(node, dist):
    for a, b in graph[node]:
        if distance[a] == -1:
            distance[a] = b + dist
            dfs(a, b + dist)


n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    nums = list(map(int, input().split()))
    for j in range(1, len(nums) - 2, 2):
        graph[nums[0]].append([nums[j], nums[j + 1]])


distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
