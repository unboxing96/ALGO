h, w = map(int, input().split())
waters = list(map(int, input().split()))

data = []
for _ in range(h):
    data.append([0 for _ in range(w)])


for i in range(h):
    for j in range(w):
        if waters[j]:
            data[i][j] += 1
            waters[j] -= 1

cnt = 0
for i in range(h):
    for j in range(w):
        if data[i][j] == 0:
            if 1 in data[i][:j] and 1 in data[i][j+1:]:
                cnt += 1

print(cnt)