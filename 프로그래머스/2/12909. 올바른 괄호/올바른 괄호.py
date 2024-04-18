# 이해
# 괄호가 올바르게 짝지어지면 True
# 하나라도 틀리면 False

# 풀이
# "("인 경우
    # stack이 비었으면 추가한다.
    # stack에 원소가 있다면, stack의 top이 "("이라면 추가. ")"이라면 return False
# ")"인 경우
    # stack이 비었으면 return False
    # stack에 원소가 있다면, stack의 top이 "("이라면 stack.pop(), ")"이라면 return False

def solution(brackets):
    stack = []
    
    for bracket in brackets:
        if bracket == "(":
            if not stack:
                stack.append(bracket)
            else:
                if stack[-1] == "(":
                    stack.append(bracket)
                else:
                    return False
        
        else: # bracket == ")"
            if not stack:
                return False
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
                
    return True if not stack else False