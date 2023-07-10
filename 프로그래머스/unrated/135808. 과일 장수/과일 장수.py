def solution(k, m, score):

    answer = 0

    result = []
    sorted_score = sorted(score, reverse=True)

    for i in range(0, len(sorted_score) + 1, m):
        result.append(sorted_score[i:i+m])

    for res in result:
        if len(res) == m:
            answer += res[-1] * m

    return answer