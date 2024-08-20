# 문제 분석
# 1. 다음 알파벳 (X -> Y -> Z -> A)
# 2. 이전 알파벳 (C -> B -> A -> Z)
# 3. 커서를 왼쪽으로 (3 -> 2 -> 1 -> 6)
# 4. 커서를 오른쪽으로 (4 -> 5 -> 6 -> 1)
# A로만 이루어진 문자열에서 출발하여, name까지 최소 이동 횟수를 return

# 접근
# 문자 이동의 관점
    # 쉽다. 순이동과 역이동 중에서 min 값을 더하면 된다.
# 커서 이동의 관점
    # JKAAANP
    # 이런 경우가 애매하다.
    # K에서는 4번 이동을 통해 N으로 넘어가는 것보다, K -> J -> P -> N으로 넘어가는 것이 빠르다.
    # AJKAAANPAA 이러한 경우는 순이동이 낫다.
    # JKAAANAPAA 이러한 경우는 순이동이 낫다.
    # JBAANAAAP
# 단순 무식한 방법
    
    
def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) # 문자 이동
        
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A': # A가 아닌 다음 문자를 찾는다.
            next_idx += 1
        
        block = len(name) - next_idx
        min_move = min(min_move, 2 * idx + block, 2 * block + idx) # 커서 이동 업데이트
        
    answer += min_move # 찾아낸 최소 커서 이동 횟수
    return answer









