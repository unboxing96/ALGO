def Rev(X):
    return int(str(X)[::-1])

a, b = map(int, input().split())
print(Rev(Rev(a)+Rev(b)))