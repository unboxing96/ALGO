import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

print(lcm(21, 14))