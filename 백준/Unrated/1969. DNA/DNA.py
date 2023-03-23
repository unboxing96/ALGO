
n, m = map(int, input().split())
data = [input() for _ in range(n)]
ans = []

for i in range(m):
    tmp = {}
    for d in data:
        if d[i] in tmp:
            tmp[d[i]] += 1
        else:
            tmp[d[i]] = 1
    ans.append(sorted(tmp.items(), key=lambda x : (-x[1], x[0]))[0][0])

string = "".join(ans)

cnt = 0
for d in data:
    for i in range(m):
        if d[i] != string[i]:
            cnt += 1

print(string)
print(cnt)