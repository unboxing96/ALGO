def solution(numbers):

    stack = [] # 뒷큰수를 찾고 있는 인덱스를 저장
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
