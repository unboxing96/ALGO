from collections import deque

## 몇 개의 노드 덩어리가 존재하는지
# 인접 리스트 생성
# 인접 리스트 개수 return

# 재귀 함수 생성
def DFS(start, stack):
    num = stack.pop()
    visited[num] = start
    for edge in adj[num]:
        if visited[edge] == 0:
            stack.append(edge)
            DFS(start, stack)



T = int(input())

for t in range(1, T+1):
    
    N, M = map(int, input().split())

    # 빈 리스트 (노드 + 1번 반복)
    adj = [[] for _ in range(N+1)] 

    # 방문 리스트 (노드 + 1번 반복)
    visited = [0 for _ in range(N+1)]

    # 인접 리스트 생성 (엣지만큼 반복)
    for i in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    cnt = 0

    # 노드 + 1번만큼 반복하며 탐색
    for i in range(1, N+1):
        if visited[i] == 0:
            DFS(i, [i])
            cnt += 1
    
    print(f"#{t} {cnt}")
