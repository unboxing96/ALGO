
while True:
    try:
        s, t = input().split()
        i = 0
        j = 0
        length_s = len(s)
        length_t = len(t)
        flag = False

        while True:

            if i >= length_s:
                flag = True
                break
            elif j >= length_t:
                break

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if flag:
            print("Yes")
        else:
            print("No")

    except EOFError:
        break

    
