
result = ""
flag = False
tmp = ""

for i in input():
    if i == "<":
        flag = True
        result += tmp[::-1]
        tmp = ""
        result += i
        continue

    elif i == ">":
        flag = False
        result += i
        continue

    elif i == " ":
        result += tmp[::-1] + " "
        tmp = ""
        continue
        
    if flag:
        result += i

    else:
        tmp += i

print(result+tmp[::-1])