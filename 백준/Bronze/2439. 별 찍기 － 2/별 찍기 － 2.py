N = int(input())
for i in range(N):
    star = "*" * (i + 1)
    space = " " * (N - 1 - i)
    print(space + star)
