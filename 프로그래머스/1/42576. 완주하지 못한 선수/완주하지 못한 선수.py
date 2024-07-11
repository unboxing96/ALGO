# 문제 분석
# participant에 참가자 배열
# completion에 완주자 배열. 참가자보다 1명 적다.
# 미완주자를 return
# 동명이인이 있다.

# 접근
# participant 배열 요소의 개수를 세는 딕셔너리participantDict를 생성한다.
# completion을 탐색하며 participantDict에서 대응하는 값을 뺀다.
# 마지막에 값이 1인 유일한 원소의 key를 출력한다.

# def solution(participant, completion):
    
#     participantDict = {}
#     for part in participant:
#         if participantDict.get(part, 0):
#             participantDict[part] += 1
#         else:
#             participantDict[part] = 1
    
#     for comp in completion:
#         participantDict[comp] -= 1
    
#     for k, v in participantDict.items():
#         if v == 1:
#             return k

def solution(participant, completion):
    answer = ""
    dict = {}
    temp = 0
    
    for part in participant:
        dict[hash(part)] = part
        temp += int(hash(part))
    
    for comp in completion:
        dict[hash(comp)] = comp
        temp -= int(hash(comp))
    
    answer = dict[temp]
    
    return answer









