while True:
    try:
        n = int(input())
    except EOFError:
        break

    target = "1"
    while True:
        if int(target) % n == 0:
            print(len(target))
            break
        else:
            target += "1"
