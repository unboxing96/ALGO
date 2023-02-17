
import sys
input = sys.stdin.readline

v = int(input().rstrip())
e = int(input().rstrip())

# parent nodes initialize
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
tot = 0

for _ in range(e):
    a, b, cost = map(int, input().rstrip().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        tot += cost

print(tot)