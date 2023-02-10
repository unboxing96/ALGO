
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선 정보 / 최소 스패닝 트리 거리
edges = []
tot_cost = 0

# 간선 정보 입력 받기
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# cost 기준 오름차순 정렬
edges.sort()

# 간선 정보 하나씩 확인하며 크루스칼 알고리즘
for i in range(e):
    cost, a, b = edges[i]
    # find 연산 -> 부모 다르면 사이클 없으므로 union 수행 -> 같으면 pass
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        tot_cost += cost

print(tot_cost)
