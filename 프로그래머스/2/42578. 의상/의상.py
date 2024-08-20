# 문제 분석
# 서로 다른 조합으로 옷을 입는 가짓수는?
# 배열은 2차원 행렬로 주어진다
    # 이름, 종류
    # 같은 이름은 없다
    # 최소 한 개의 의상은 입어야 한다

# 접근
# 각 종류마다 "입지 않는다" 경우의 수를 추가하여 모든 가짓수를 곱한다.
# 전부 입지 않는 경우를 뺀다.

def solution(clothes):
    answer = 0
    
    hashMap = {}
    
    for cloth in clothes:
        name, category = cloth[0], cloth[1]
        if hashMap.get(category, 0):
            hashMap[category] += 1
        else:
            hashMap[category] = 1
    
    tmp = 1
    for v in hashMap.values():
        tmp *= (v + 1)
    
    return tmp - 1