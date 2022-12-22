a, b = map(int, input().split())

data = []

for i in range(1, b + 1):
    data.extend([i] * i)

print(sum(data[a - 1 : b]))