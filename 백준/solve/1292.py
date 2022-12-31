a, b = map(int, input().split())

data = []
data2 = []

for i in range(1, b + 1):
    data.extend([i] * i)
    data2.append([i] * i)

print(sum(data[a - 1 : b]))