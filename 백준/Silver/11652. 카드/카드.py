n = int(input())
dict = {}

for _ in range(n):
    num = int(input())
    if dict.get(num, 0):
        dict[num] += 1
    else:
        dict[num] = 1

MAX = max(dict.values())
print(sorted(dict.items(), key=lambda x : (-x[1], x[0]))[0][0])