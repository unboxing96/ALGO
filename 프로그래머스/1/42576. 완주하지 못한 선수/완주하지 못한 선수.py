# 이해
# completion에 있지만, participant에 없는 사람 return
# 동명이인이 있을 수 있다.
# 딕셔너리로는 애매할 듯?
# set도 애매하겠다.
# 선형 탐색으로 중복된 이름을 찾는다.
# 딕셔너리로 체크한다.
# 모든 값이 체크되면, 중복된 이름을 return 하고 아니라면, 체크되지 않은 이름을 return 한다.

# 정렬한다.
# 순서대로 나오지 않으면 즉시 return 한다.

# def solution(participant, completion):
    
#     dic = {}
#     tmp = 0
    
#     for part in participant:
#         dic[hash(part)] = part
#         tmp += hash(part)
    
#     for comp in completion:
#         tmp -= hash(comp)
        
#     return dic[tmp]

from collections import defaultdict

def solution(participant, completion):
    
    dic = defaultdict(int)
    
    for part in participant:
        dic[part] += 1
        
    for comp in completion:
        dic[comp] -= 1
    
    
    answer = ""
    for key, val in dic.items():
        if val == 1:
            answer = key
    
    return answer