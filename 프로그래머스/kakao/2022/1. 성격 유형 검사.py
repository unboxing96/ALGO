survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

# 질문 개수만큼 반복
# 점수 카운트 dict를 생성하여, 
    # "1" : {"R" : 0, "T" : 0},
    # "2" : {"C" : 0, "F" : 0},
# 각 survey 대답의 점수를 기록
# dict를 다시 반복하며, 
    # 큰 값의 키를 answer에 추가
    # 같으면 ascii로 비교 후 추가


def solution(survey, choices):

    # 값을 기록할 딕셔너리 생성
    dic = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0,
    }

    # choices 개수만큼 반복하며, 딕셔너리에 기록
    for i in range(len(choices)):
        # 응답이 3보다 크면, 뒤의 성격 유형에 -3 뺀 만큼 점수 더하기
        if choices[i] > 4:
            dic[survey[i][1]] += (choices[i] - 4)
        # 응답이 3보다 작으면, 앞의 성격 유형에 abs(4 - 값) 점수 더하기
        elif choices[i] < 4:
            dic[survey[i][0]] += (4 - choices[i])
        # 같으면 pass        
        elif choices[i] == 4:
            pass

    result = []

    # 성격 유형 고르기 함수
    def pick(a, b):
        if dic[a] != dic[b]:
            result.append(max(a, b, key= lambda x : dic[x]))
        elif dic[a] == dic[b]:
            result.append(chr(min(ord(a), ord(b))))

    # 4번 반복하며 성격 유형 고르기
    pick("R", "T")
    pick("C", "F")
    pick("J", "M")
    pick("A", "N")

    answer = ""
    for i in result:
        answer += i

    return answer