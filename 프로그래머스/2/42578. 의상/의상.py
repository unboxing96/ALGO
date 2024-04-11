# 이해
# 패션 조합의 가짓수
# 하루에 최소 한 개의 의상
# 한 종류에서는 하나의 옷만 선택
# 모든 종류를 선택할 수도, 하나의 종류만 선택할 수도, 복수의 종류만 선택할 수도 있다.

# 풀이
# from itertools import combinations
# type별로 카운트 횟수를 딕셔너리에 기록함
# type에 대한 조합을 구함.
# 모든 조합에 대하여, type에 대응하는 카운트 횟수를 곱해 answer에 더함.
# answer 반환.

def solution(clothes):
    answer = 1  # 곱셈을 위해 1부터 시작
    dic = {}
    
    # 각 옷의 종류별로 개수를 계산
    for _, type in clothes:
        dic[type] = dic.get(type, 0) + 1
    
    # 각 종류별로 옷을 선택하는 경우의 수 계산 (해당 종류의 옷을 안 입는 경우 포함)
    for count in dic.values():
        answer *= (count + 1)  # 해당 종류의 옷을 선택하지 않는 경우도 포함하여 +1
    
    return answer - 1  # 아무것도 입지 않는 경우의 수 1을 뺌
