bracket = input()

stack = []
tmp = 1
res = 0

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2
    
    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3
    
    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        elif bracket[i-1] == "(":
            res += tmp
        tmp //= 2
        stack.pop()
    
    else: # bracket[i] == "]":
        if not stack or stack[-1] == "(":
            res = 0
            break
        elif bracket[i-1] == "[":
            res += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(res)