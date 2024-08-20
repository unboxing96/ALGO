import sys
sys.stdin = open("test.txt")

from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = False
    
    while q:
        x = q.popleft()
        print(x, end = " ")
        
        for next_node in matrix[x]:
            if visited[next_node]:
                visited[next_node] = False
                q.append(next_node)

def dfs(start):
    
    # 스택 초기화
    stack = [start]
    
    while stack:
        node = stack.pop() # 스택에서 노드를 하나 꺼냄
        
        # if not visited[node]:
        visited[node] = True
        print(node, end = " ")
        
        # 현재 노드의 인접 노드를 스택에 추가
        # 인접 노드들을 역순으로 추가하여 탐색 순서를 보장합니다.
        for neighbor in reversed(matrix[node]):
            if not visited[neighbor]:
                stack.append(neighbor)

    
n, m, v = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for m in matrix:
    m.sort()
    
dfs(v)
print()
bfs(v)