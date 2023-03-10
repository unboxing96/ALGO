import sys
sys.stdin = open("1647.txt", "r")

###

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x : x[2])

parent = [i for i in range(v+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

select = []

answer = 0
for a, b, cost in edges:
    # cycle = True
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost
        select.append(cost)
    
answer -= select.pop()
print(answer)