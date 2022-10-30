def sam(number):
    cnt = 0

    for num in range(1, number + 1):

        num = str(num)

        for i in num:
            if i in "369":
                cnt += 1

    return cnt


number = 33

result = sam(number)
print(result)
