def solution(s):

    low_s = s.lower()

    if low_s.count("p") == low_s.count("y"):
        answer = True
    else:
        answer = False

    return answer


s = "ooo"
print(solution(s))
