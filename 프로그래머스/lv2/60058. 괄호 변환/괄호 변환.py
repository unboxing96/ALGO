def solution(p):

    # 1
    if not p:
        return ""

    # 2
    u, v = divide(p)

    # 3
    if check_best(u):
        return u + solution(v)

    # 4
    else:
        ans = "("
        ans += solution(v)
        ans += ")"
        for p in u[1 : len(u) - 1]:
            if p == "(":
                ans += ")"
            else:
                ans += "("
    return ans


def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return p[: i + 1], p[i + 1 :]


def check_best(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


p = "()))((()"
print(solution(p))
