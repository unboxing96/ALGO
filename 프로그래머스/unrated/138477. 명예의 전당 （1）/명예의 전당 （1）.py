def solution(k, score):
    answer = []

    stack = []

    for sco in score:
        if len(stack) < k:
            stack.append(sco)
        else:
            if stack[-1] < sco:
                stack.pop()
                stack.append(sco)
        stack.sort(reverse=True)
        answer.append(stack[-1])

    return answer