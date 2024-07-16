# 문제 분석
# 각 수포자는 일정한 패턴으로 답을 찍는다.
# 정답 배열이 주어지면, 패턴과 답을 맞춰보며 점수를 기록한다
# 최고점을 기록한 수포자의 인덱스를 return 한다.
# 동점자가 있으면, 인덱스의 오름차순으로 return 한다.

# 접근
# 각 수포자 패턴에 대하여 길이가 10,000 이상인 배열을 생성한다.
# 정답을 맞춰보아, 각 수포자의 점수를 기록한다.
# 점수의 max 값을 구하고, 인덱스 순서대로 배열을 탐색하며, max와 점수와 같은 것을 배열에 삽입한다.
# 배열을 return한다.

def solution(answers):
    answer = []
    
    s1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] * 1000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] * 1000
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    scores = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        if s1[idx] == ans:
            scores[0] += 1
        
        if s2[idx] == ans:
            scores[1] += 1
        
        if s3[idx] == ans:
            scores[2] += 1
    
    maxScore = max(scores)
    
    for idx, score in enumerate(scores):
        if score == maxScore:
            answer.append(idx + 1)
    
    return answer