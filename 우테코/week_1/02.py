def joongbok(cryptogram):

    while True:

        tmp = []

        for i in range(len(cryptogram)):
            if tmp:
                if cryptogram[i - 1] == cryptogram[i]:
                    tmp.pop()
                    continue

            tmp.append(cryptogram[i])

        cryptogram = tmp

        if len(set(cryptogram)) == len(cryptogram):
            return "".join(cryptogram)


cryptogram = "browoanoommnaon"

result = joongbok(cryptogram)
print(result)
