# range(1, len(stages)+1) 만큼 반복
# score = {}
# left = len(stages)
# 실패율 = count(i) / left
# 딕셔너리 키 있으면 실패율 값 추가, 없으면 생성하고 실패율 값 추가
#  score[i] = count(i) / left
# 실패율 값 -= 카운트 값

# 연산 종료
# score dict 순환
# 1. values 순환하며 내림차순 sort
# 2. key 순환하며 오름차순 sort


def solution(N, stages):

    score = {}
    left = len(stages)
    for i in range(1, N + 1):  # 남은 사람 있으면 고고
        if left != 0:
            score[i] = stages.count(i) / left  # 딕셔너리에 실패율 값 추가
            left -= stages.count(i)  # 남은 사람에서 해당 스테이지 통과한 사람 빼기
        else:
            score[i] = 0

    answer = []

    for i in sorted(score.items(), key=lambda x: (-x[1], x[0])):
        answer.append(i[0])

    return answer


# 값 실행하는 부분
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
