# 풀이 시간: 16:19 ~

# {성격1: 점수, 성격2: 점수, 성격3: 점수, ...}
# answer_dict에 현재 성격 유형이 없으면 현재 값으로 초기화, 있으면 기존 값에 더하기
# ["RT", "CF", "JM", "AN"] 배열을 탐색하며, 각 원소의 앞 문자와 뒷 문자의 점수 중에 높은 것을 answer에 추가하기

from collections import defaultdict

answer_string = ["RT", "CF", "JM", "AN"]
answer_dict = defaultdict(int)

def solution(survey, choices):
    answer = ''
    
    # score_dict에 점수 업데이트 하기
    for i in range(len(survey)):
        survey_elem = survey[i] # AN
        
        # 선택 분석
        score = choices[i]
        
        # 앞 문자를 선택한 경우
        if score <= 3:
            score_to_add = 4 - score
            
            # 앞 문자
            answer_dict[survey_elem[0]] += score_to_add # 더하기
        
        # 뒷 문자를 선택한 경우
        if score >= 5:
            score_to_add = score - 4
            
            # 뒷 문자
            answer_dict[survey_elem[1]] += score_to_add #더하기
        
    # 결과 출력하기
    for i in range(len(answer_string)):
        answer_string_elem = answer_string[i]

        if answer_dict[answer_string_elem[0]] > answer_dict[answer_string_elem[1]]:
            answer += answer_string_elem[0]
            
        elif answer_dict[answer_string_elem[0]] < answer_dict[answer_string_elem[1]]:
            answer += answer_string_elem[1]
        
        else:
            answer += sorted(answer_string_elem)[0]
    
    return answer