A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

if A_list == B_list:
    print(10, 10)
    print("D")
else:
    a = 0
    b = 0
    for i in range(10):
        if A_list[i] > B_list[i]:
            a += 3
            win = "A"
        elif A_list[i] < B_list[i]:
            b += 3
            win = "B"
        else:
            a += 1
            b += 1
    print(a, b)
    if a == b:
        print(win)
    else:
        print("A" if a > b else "B")
