a, b, c = map(int, input().split())

if b >= c:
    print("-1")
else:
    earn = c - b
    print(a // earn + 1)
