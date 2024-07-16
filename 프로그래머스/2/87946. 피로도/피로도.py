# 문제 분석
# 각 던전마다 ['최소 필요 피로도', '소모 피로도']가 있다.
# 하루에 최대한 많은 던전을 방문하고자 한다.

# 접근
# dungeons의 개수는 최대 8이다.
# 순열을 구하면 O(N!) -> O(8!) ~= 40,000
# 가능한 조합을 구하고, 최대 던전 방문 횟수를 계산한다.

candidates = []

def solution(k, dungeons):
    global candidates
    
    answer = -1
    visited = [False] * len(dungeons)
    permutation(dungeons, visited, [])
    
    for cand in candidates:
        tempK = k
        cnt = 0

        for stage in cand:
            if tempK >= stage[0]:
                tempK -= stage[1]
                cnt += 1
                
        answer = max(answer, cnt)

    return answer


def permutation(dungeons, visited, perm):
    global candidates

    if len(perm) == len(dungeons):
        candidates.append(perm[:])
        return
    
    for i in range(len(dungeons)):
        if not visited[i]:
            visited[i] = True
            perm.append(dungeons[i])
            permutation(dungeons, visited, perm)
            perm.pop()
            visited[i] = False
        
        
        
        