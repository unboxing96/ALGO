# 이해
# 네트워크(연결된 덩어리)의 개수를 return

# 풀이
# 각 노드에 대한 visited 배열 생성
# computers 탐색
# 현재 노드를 방문하지 않았다면, dfs 진행
# 탐색이 종료되면 cnt += 1
# cnt를 return

def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)
    
    for i in range(len(computers)):
        if not visited[i]:
            print("GO DFS")
            answer += dfs(i, computers, visited)
    
    return answer

def dfs(n, computers, visited):
    print(f"Node: {n}")
    visited[n] = True
    
    for idx, next in enumerate(computers[n]):
        if not visited[idx] and next == 1:
            dfs(idx, computers, visited)
    
    return 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    