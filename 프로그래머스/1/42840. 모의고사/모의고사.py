# 풀이
# 각 수포자의 패턴을 반복하는 배열을 만듦. 10000개까지.
# 가장 패턴의 길이가 짧은 수포자 1을 기준으로 하여, 2000번씩 반복함
# 반복문으로 answers를 탐색하며, 각 수포자의 점수를 계산
# 최고점을 맞은 수포자를 배열로 return

# 의사코드
# one_array = [1, 2, 3, 4, 5] * 2000
# two_array = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
# three_array = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
# one_score = 0
# two_score = 0
# three_score = 0
# for i in range(len(answers)):
# if one_array[i] == answers[i]:
# one_score += 1
# ...
# top_score = max(one_score, ...)
# score_array = [one_score, two_score, three_score]
# for i in range(3):
# if score_array[i] == top_score:
# answer.append(i + 1)

def solution(answers):
    answer = []
    
    one_array = [1, 2, 3, 4, 5] * 2000
    two_array = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    three_array = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    one_score = 0
    two_score = 0
    three_score = 0
    
    for i in range(len(answers)):
        if one_array[i] == answers[i]:
            one_score += 1
        if two_array[i] == answers[i]:
            two_score += 1
        if three_array[i] == answers[i]:
            three_score += 1

    top_score = max(one_score, two_score, three_score)
    score_array = [one_score, two_score, three_score]
    
    for i in range(3):
        if score_array[i] == top_score:
            answer.append(i + 1)
    
    return answer