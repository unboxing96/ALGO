
def separate(w):
    open_count = 0
    close_count = 0
    for idx, elem in enumerate(w):
        if elem == "(":
            open_count += 1
        else:
            close_count += 1
        
        if open_count == close_count:
            return w[:idx+1], w[idx+1:]

def perfection_check(u):
    stack = []
    for elem in u:
        if elem == "(":
            stack.append(elem)
        elif elem == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def make_perfection(u, v):
    tmp = "("
    tmp += solution(v)
    tmp += ")"
    for s in u[1:len(u)-1]:
        if s == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp

def solution(p):
    if len(p) == 0:
        return ""

    u, v = separate(p)

    if perfection_check(u):
        return u + solution(v)
    else:
        return make_perfection(u, v)

p = "()))((()"
result = solution(p)
print(result)
