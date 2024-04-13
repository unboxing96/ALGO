# 이해
# 연결 관계를 나타내는 wires가 주어짐
# wires 중에 하나를 제거했을 때, 나누어진 두 전력망의 차이(절댓값)의 최솟값을 return

# 풀이
# wires의 원소를 하나씩 빼고 연결 그래프를 생성
# 연결 그래프의 첫 번째 노드를 시작으로, 연결된 네트워크의 크기를 구함
# 두 개 네트워크의 크기의 차이로 갱신

def solution(n, wires):
    diff = int(1e9)
    
    def dfs(now, graph, visited):
        visited[now] = True
        cnt = 1
        
        for neighbor in graph[now]:
            if not visited[neighbor]:
                cnt += dfs(neighbor, graph, visited)
        
        return cnt
    
    
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)
        size_one_network = dfs(a, graph, visited)
        current_diff = abs((n - size_one_network) - size_one_network)
        diff = min(diff, current_diff)

        graph[a].append(b)
        graph[b].append(a) # 그래프 원상복구
        
    return diff


