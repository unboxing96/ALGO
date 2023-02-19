
# union-find algorithm
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# union-find
n = int(input())
m = int(input())
parent = [i for i in range(n)]
for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union_parent(parent, i, j)


# 경로 체크
parent = [-1] + parent
path = list(map(int, input().split()))
start = parent[path[0]]

for i in range(1, m):
    if parent[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
