# 이해
# begin을 target으로 만들어야 한다. 둘은 반드시 다르다. 
# 이동 규칙은 words에서 한 글자만 달라지는 원소를 찾아서 이동할 수 있다.
# 최소 이동 횟수를 구해야 한다. BFS? DFS인 듯. 깊이를 추적해야 함.
# 변환할 수 없는 경우에는 0을 return 한다. 모든 word를 이동한 경우 or 이동할 수 있는 word가 없는 경우

# 풀이
# 방문 처리할 visited 배열을 만든다.
# 최소 깊이를 저장할 min_depth = int(1e9)
# dfs로 탐색한다.
    # 탈출 조건: target를 찾은 경우. 이때 깊이를 갱신한다.
# 정답을 못 찾은 경우, 이동할 수 있는 word가 없는 경우, target이 word에 없는 경우 0을 반환한다.

# dfs(node, visited, depth, min_depth)

# if new_node == target:
    # min_depth = min(depth, min_depth)
    # return min_depth
    
# words 배열을 탐색한다.
    # 방문하지 않았고, 현재 노드와 한 글자 차이나는 경우 
    # 이 노드를 방문처리 한다.
    # 방문 처리한 배열을 복사한다.
    # dfs(new_node, 복사한 visited, depth+1)를 재귀적으로 호출한다.

# return 0 # 이동할 수 없는 경우, 다 돌았는데 정답을 못 찾은 경우

def solution(begin, target, words):
    
    INF = int(1e9)
    min_depth = [INF]
    visited = [False] * (len(words))
    
    dfs(begin, target, words, visited, 0, min_depth)
    
    return min_depth[0] if min_depth[0] != INF else 0


def checkAvailability(node, word):
    cnt = 0
    for i in range(len(node)):
        if node[i] != word[i]:
            cnt += 1
    return cnt == 1
    

def dfs(node, target, words, visited, depth, min_depth):
    
    if node == target:
        min_depth[0] = min(min_depth[0], depth)
        return
    
    for idx, word in enumerate(words):
        if visited[idx]: # 이미 방문했다면 pass
            continue
        
        if checkAvailability(node, word): # 한 글자만 차이나는지 확인
            visited[idx] = True
            dfs(word, target, words, visited, depth+1, min_depth)
            visited[idx] = False
    
    
    
    
    
    