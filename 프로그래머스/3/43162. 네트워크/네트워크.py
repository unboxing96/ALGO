# 풀이: BFS
# 연결 요소를 탐색하기 위해서는 DFS/BFS 모두 좋다.
# 파이썬에서 큐는 deque으로 구현한다.
# 각 컴퓨터에 대한 visited 배열을 생성한다.
# 인접 행렬을 탐색한다. 방문하지 않은 행(노드)을 만나면 bfs를 진행한다.
    # bfs()
        # 현재 노드를 방문 처리한다.
        # 큐를 deque()으로 초기화하고, 현재 노드를 추가한다.
        # 큐가 빌 때까지 반복한다.
        # 큐에서 pop한다.
        # pop한 노드의 인접 노드를 아직 방문하지 않았다면, 큐에 추가한다. 방문 처리한다.
    # bfs가 종료되면 cnt += 1한다.
# cnt를 return 한다.

from collections import deque

def solution(n, computers):

    # 각 컴퓨터에 대한 visited 배열을 생성한다.
    visited = [False] * n
    cnt = 0
    
    # bfs()
    def bfs(start):
        # 현재 노드를 방문 처리한다.
        # 큐를 deque()으로 초기화하고, 현재 노드를 추가한다.
        visited[start] = True
        queue = deque([start])
        
        # 큐가 빌 때까지 반복한다.
        while queue:
            # 큐에서 pop한다. 방문 처리한다.
            v = queue.popleft()
            
            for i in range(n):
                # pop한 노드의 인접 노드를 아직 방문하지 않았고 연결되었다면, 큐에 추가한다. 
                if not visited[i] and computers[v][i] == 1:
                    queue.append(i)
                    visited[i] = True
    
    # 인접 행렬을 탐색한다. 방문하지 않은 행(노드)을 만나면 bfs를 진행한다.
    for i in range(n):
        if not visited[i]:
            bfs(i)
            # bfs가 종료되면 cnt += 1한다.
            cnt += 1
    
    return cnt








