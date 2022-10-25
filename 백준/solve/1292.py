a, b = map(int, input().split())

data = []
cnt = 1

while len(data) < b:
    for i in range(cnt):
        data.append(cnt)
    cnt += 1

print(sum(data[a-1:b]))