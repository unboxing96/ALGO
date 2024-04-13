# 이해
# 모음으로 길이 5 이하의 모든 단어가 기록된 사전
# 해당 사전에서 word가 몇 번째 단어인지 출력

# 풀이
# 모음으로 만들 수 있는 모든 조합을 생성 -> 중복 조합이 필요
# 조합을 정렬
# return 입력된 단어의 index + 1

from itertools import product

def solution(word):
    answer = 0
    candidates = []
    
    for i in range(1, 6):
        candidates.extend(list(map(lambda x: "".join(x), product("AEIOU", repeat = i))))
    
    candidates.sort()
    
    return candidates.index(word) + 1