# 이해
# 연결 관계가 적힌 티켓이 주어진다.
# 티켓의 정보를 모두 입력하면, 한 덩어리로 이루어진 연결 요소이다.
# 한 시점에서 방문 가능 경로가 여러가지라면, 알파벳 순으로 앞선 것을 선택한다.
# 모든 국가를 방문하는 경로를 출력하라.

# 풀이
# 모든 경로를 탐색해야 하므로 DFS, BFS 상관 없지 않을까?
# 백트래킹을 하기 위한 DFS가 더 적합하겠다.

def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    dfs("ICN", ["ICN"], tickets, visited, answer)
    return sorted(answer)[0]


def dfs(airport, path, tickets, visited, answer):
    if len(path) == len(tickets) + 1:
        answer.append(path)
        return
    
    for i, ticket in enumerate(tickets):
        if ticket[0] == airport and not visited[i]:
            visited[i] = True
            dfs(ticket[1], path + [ticket[1]], tickets, visited, answer)
            visited[i] = False
            
            
            
    
    
    