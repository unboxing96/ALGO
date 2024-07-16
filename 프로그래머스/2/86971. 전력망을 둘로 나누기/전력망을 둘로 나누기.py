# 접근
# 모든 노드를 연결한다
# 입력으로 주어진 wires를 탐색하며 각 연결을 삭제하고, 탐색하여 answer를 갱신하고, 다시 연결한다.

# 탐색은?
# 어차피 모든 노드를 탐색해야 해서 DFS, BFS의 차이는 없을 것 같다.
# 매번 visited 배열을 초기화 하면서, 현재 노드를 방문하지 않았으면 dfs 혹은 bfs를 하면 되겠다.
# dfs로 하자.


def dfs(start, graph, visited, check_link):
    cnt = 1
    visited[start] = True
    
    for adj_node in graph[start]:
        if not visited[adj_node] and check_link[start][adj_node]:
            cnt += dfs(adj_node, graph, visited, check_link)
    
    return cnt

def solution(n, wires):
    answer = 10000000
    
    check_link = [[True] * (n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n+1)
        check_link[a][b] = False
        cnt_a = dfs(a, graph, visited, check_link)
        cnt_b = dfs(b, graph, visited, check_link)
        check_link[a][b] = True
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer