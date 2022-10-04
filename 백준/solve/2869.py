a, b, v = map(int, input().split())

result = (v - b) // (a - b)
print(result if result == 0 else result + 1)
