import sys

numbers = sys.stdin.readlines()

for num in numbers:
    a, b = num.split()
    a = int(a)
    b = int(b)
    print(a + b)
