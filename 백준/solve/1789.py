s = int(input())

res = 0
cnt = 1
while res <= s:
    res += cnt

    if res <= s:
        cnt += 1

print(cnt - 1)
