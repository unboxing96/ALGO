# 이해
# 스택에 연속된 숫자가 저장되면 안 됨.

# 풀이
# arr을 탐색하며 stack에 추가
# 추가하기 전, stack의 top과 같은 경우 pass, 다른 경우 push

def solution(arr):
    stack = []
    
    for elem in arr:
        if stack:
            if elem != stack[-1]:
                stack.append(elem)
        else:
            stack.append(elem)
    
    return stack