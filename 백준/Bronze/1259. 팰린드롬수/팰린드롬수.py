while True:
    num = input()

    if num == "0":
        break

    n = len(num)

    if n % 2 == 0:
        if num[0 : n // 2][::-1] == num[n // 2 : n]:
            print("yes")
        else:
            print("no")
    else:
        if num[0 : n // 2][::-1] == num[n // 2 + 1 : n]:
            print("yes")
        else:
            print("no")