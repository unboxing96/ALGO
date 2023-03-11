import sys
sys.stdin = open("1717.txt", "r")

"""
n+1개의 집합
m개의 연산
0 a b -> a, b 합친다 (union)
1 a b -> a, b 부모를 찾는다 (find) -> 집합에 포함되어 있으면 YES / 없으면 NO
"""

import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    order, a, b = map(int, input().split())

    if order == 0:
        union_parent(a, b)
    else: # order == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
            