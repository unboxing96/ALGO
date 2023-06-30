def solution(food):
    answer = ""

    for i in range(1, len(food)):
        size = food[i] // 2
        answer += str(i) * size

    tmp = answer
    answer += "0"
    answer += tmp[::-1]

    return answer