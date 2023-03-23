
n = input()
data = list(map(int, n))

if sum(data) % 3 == 0:
    number = int("".join(map(str, sorted(data, reverse=True))))
    if number % 10 == 0:
        print(number)
    else:
        print(-1)
else:
    print(-1)