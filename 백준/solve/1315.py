n = int(input())

cnt = 0

for tc in range(n):
    test = []
    word = input()
    for i in word:
        if len(test) != 0:
            if i in test:
                if i != test[-1]:
                    break
        test.append(i)
    else:
        cnt += 1

print(cnt)
