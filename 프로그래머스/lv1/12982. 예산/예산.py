def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)

    for i in range(len(sorted_d)):
        if budget >= sorted_d[i]:
            budget -= sorted_d[i]
            answer += 1
        else:
            break

    return answer