# 이해
# 현재 피로도 k
# dungeons의 원소는 첫 항은 필요 피로도, 두 번쨰 항은 소모 피로도
# 유저가 탐험할 수 있는 최대 던전 수를 return

# 풀이
# dungeons의 모든 순열을 구하고 각 순열을 테스트
# 최대 길이는 8이므로, 가능한 순열의 수는 8! ~= 40,000
# O(N ** 2)으로 작성하면 1,600,000,000 이어서 안 될 것 같지만, 프로그래머스니까 해보자 !

# from itertools import permutations

# def solution(k, dungeons):
#     answer = -1
    
#     perms = list(permutations(dungeons, len(dungeons)))
    
#     for perm in perms:
#         tmp = k
#         cnt = 0
#         for need, use in perm:
#             if tmp >= need:
#                 tmp -= use
#                 cnt += 1
#             else:
#                 break
        
#         answer = max(answer, cnt)
    
#     return answer


def solution(k, dungeons):
    
    def dfs(k, cnt, dungeons):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                dfs(k - dungeons[i][1], cnt + 1, dungeons)
                visited[i] = False
    
    answer = -1
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons)
    
    return answer








