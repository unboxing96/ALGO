# 10을 다른 문자로 교체
# dartResult 반복하다가,
# isnumberic()으로 숫자 만나면,
# int로 형변환 후, stack에 넣음
# SDT 만나면,
# stack에서 꺼내, 값을 계산 후 answer에 append
# * 만나면
# answer 길이가 1보다 크면, [-2]와 [-1]에 *= 2
# answer 길이가 1이하 이면, [-1]에 *= 2
# # 만나면
# [-1] *= -1
# sum(answer)


def solution(dartResult):

    answer = []
    stack = []

    dartResult.replace("10", "k")

    for txt in dartResult:
        if txt.isnumeric():
            stack.append(int(txt))

        elif txt == "k":
            stack.append(10)

        elif txt == "S":
            num = stack.pop()
            answer.append(num * 1)

        elif txt == "D":
            num = stack.pop()
            answer.append(num**2)

        elif txt == "T":
            num = stack.pop()
            answer.append(num**3)

        elif txt == "*":
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= 2

        elif txt == "#":
            answer[-1] *= -1

    return sum(answer)


dartResult = "1D2S#10S"
print(solution(dartResult))
