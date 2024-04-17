# 이해
# 주어진 항공권을 모두 이용
# 항상 "ICN" 공항에서 출발
# 가능한 경로가 2개 이상일 경우 알파벳 빠른 순으로 -> 정렬
# 반드시 모든 도시 방문 가능

# 풀이
# DFS 백트래킹 ?
# DFS
    # 탈출 조건
    # 모든 tickets을 방문 (방문할 때마다 cnt)
        # answer 후보로 추가

# ticket의 [1]에 해당하는 값을 tickets에서 찾는다. 
    # 해당 노드를 방문하지 않은 경우 dfs(cnt + 1).

answer = []
    
def solution(tickets):
    visited = [False] * len(tickets)
    dfs(tickets, visited, "ICN", ["ICN"])
    return sorted(answer)[0]

def dfs(tickets, visited, now, candidate):
    global answer
    if len(candidate) == len(tickets) + 1:
        answer.append(candidate)
    
    for i, ticket in enumerate(tickets):
        if now == ticket[0] and not visited[i]:
            visited[i] = True
            dfs(tickets, visited, ticket[1], candidate + [ticket[1]])
            visited[i] = False
            
    
    
    
    
    
    
    