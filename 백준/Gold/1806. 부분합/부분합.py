
n, s = map(int, input().split())
num_list = list(map(int, input().split()))

i = 0
j = 0
ans = 100001
prefix = num_list[0]

while True:
    if prefix >= s:
        ans = min(ans, j - i + 1)
        prefix -= num_list[i]
        i += 1
    else:
        j += 1

        if j == n:
            break

        prefix += num_list[j]

if ans == 100001:
    print(0)
else:
    print(ans)