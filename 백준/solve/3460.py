t = int(input())

for _ in range(t):
    num = bin(int(input()))[2:][::-1]
    for i in range(len(num)):
        if num[i] == "1":
            print(i, end=" ")