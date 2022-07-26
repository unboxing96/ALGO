a, b = map(int, input().split())

def gcb(a, b):
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b

def lcm(a, b):
    return a * b // gcb(a, b)

print(gcb(a, b))
print(lcm(a, b))
