N = int(input())

for i in range(N):
    OX = input()
    cnt = 0
    plus = 0
    for j in range(len(OX)):
        if OX[j] == "O":
            cnt += 1
            plus += cnt
        elif OX[j] == "X":
            cnt = 0
    print(plus)