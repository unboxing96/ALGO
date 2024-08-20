# 문제 분석
# 그 괄호 문제
# (는 여는 것이다.
# )는 닫는 것이다.
# 열었으면 모조리 닫아야 한다.
# 열려있는 것이 없는데 닫으면 false.
# 열려있는 것을 모두 닫지 못 하면 false.

# 접근
# "("를 만나면 stack에 추가한다.
# ")"를 만나면 고민한다.
    # stack이 비어있으면 false
    # stack의 top이 ")"이면 false
    # stack의 top이 "("이면 stack.pop()
# 탐색을 종료했을 때 stack에 값이 남아있으면 false
# 나머지는 true

def solution(s):
    answer = True
    stack = []
    
    for elem in s:
        if elem == "(":
            stack.append("(")
        elif not stack or stack[-1] == ")":
            return False
        elif stack[-1] == "(":
            stack.pop()
    
    if stack:
        return False
    else:
        return True