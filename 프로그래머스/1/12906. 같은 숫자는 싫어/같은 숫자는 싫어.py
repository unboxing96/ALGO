def solution(arr):
    answer = []
    stack = []
    
    for elem in arr:
        if stack:
            if elem != stack[-1]:
                answer.append(elem)
                stack.append(elem)
        else:
            answer.append(elem)
            stack.append(elem)
                
    return answer