word = input()

result = []

while True:
    word = input()

    if word == "문제":
        result.append(word)
    
    elif word == "고무오리":
        if len(result) != 0:
            result.pop()
        else:
            result.append(word)
            result.append(word)
    
    else:
        if len(result) == 0:
            print("고무오리야 사랑해")
        else:
            print("힝구")
        break
