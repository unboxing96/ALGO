T = int(input())

for _ in range(T):
    words = input().split()
    new = []
    for word in words:
        new.append(word[::-1])
    print(*new)