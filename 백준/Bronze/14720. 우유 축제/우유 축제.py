T = int(input())

store = list(map(int, input().split()))

milk = 0
cnt = 0

for i in range(len(store)):
    if milk == store[i]:
        milk += 1
        cnt += 1
        if milk > 2:
            milk = 0

print(cnt)