n = int(input())

coins = [25, 10, 5, 1]

for i in range(n):
    target = int(input())
    cnt = []
    for c in coins:
        cnt.append(int(target // c))
        target %= c
    print(*cnt, sep=" ")
