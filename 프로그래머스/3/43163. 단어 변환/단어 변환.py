# 이해
# begin에서 출발해서 target으로 도착하기 까지 최소 단계를 return
# 이동은 words의 단어로 변환하는 것만 가능하다. 한 글자만 다른 경우 이동이 가능하다.
# 변환할 수 없는 경우 return 0

# 풀이
# 최소 단계이나 DFS도 가능할 듯하다.
# visited를 생성한다.
# DFS
    # 탈출 조건은 target이 달성된 경우.
        # 이동 횟수를 최소값으로 갱신한다.
    # for word in words
    # 현재 word를 방문하지 않았다면,
        # 현재 word를 방문 처리
        # dfs(cnt + 1)

INF = int(1e9)
answer = INF

def solution(begin, target, words):
    visited = [False] * len(words)
    dfs(begin, target, words, visited, 0)
    return 0 if answer == INF else answer

def dfs(begin, target, words, visited, cnt):
    global answer
    if begin == target:
        answer = min(answer, cnt)
    
    for idx, word in enumerate(words):
        if not visited[idx] and check(begin, word):
            visited[idx] = True
            dfs(word, target, words, visited, cnt + 1)
            visited[idx] = False

def check(a_word, b_word):
    tmp = 0
    for i in range(len(a_word)):
        if a_word[i] != b_word[i]:
            tmp += 1
    
    return True if tmp == 1 else False
    
    
    
    
    
    
    
    
    