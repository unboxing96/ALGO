n = int(input())
m = int(input())


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# union - find
parent = [i for i in range(n)]
mat = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            union(i, j)

# 끊어진 연결 확인하기
path = list(map(int, input().split()))
parent = [-1] + parent
start = parent[path[0]]

for i in range(1, m):
    if start != parent[path[i]]:
        print("NO")
        break
else:
    print("YES")
