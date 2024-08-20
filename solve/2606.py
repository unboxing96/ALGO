import sys
sys.stdin = open("2606.txt", "r")

def bfs(v):
    q = deque([v])
    cnt = 0

    while q:
        x = q.popleft()
        visited[x] = True

        for next in matrix[x]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    
    return cnt

from collections import deque

n = int(input())
coms = int(input())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(coms):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

print(bfs(1))