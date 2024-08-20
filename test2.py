def dfs_stack(graph, start):
    
    # 스택 초기화
    stack = [start]
    
    while stack:
        node = stack.pop() # 스택에서 노드를 하나 꺼냄
        
        if not visited[node]:
            visited[node] = True
            print(node, end = " ")
            
            # 현재 노드의 인접 노드를 스택에 추가
            # 인접 노드들을 역순으로 추가하여 탐색 순서를 보장합니다.
            for neighbor in reversed(graph[node]):
                # if not visited[neighbor]:
                stack.append(neighbor)

# 예제 그래프: 인접 리스트로 표현 
# 가정1: 노드는 1부터 시작
# 가정2: 오름차순으로 정렬되어 있음
graph = [[], [2, 3], [1, 4, 5], [1, 6], [2], [2, 6], [3, 5]]

n = len(graph)
visited = [False] * (n + 1)

# DFS 실행
dfs_stack(graph, 1)

# 출력 예시
# 1 2 4 5 6 3