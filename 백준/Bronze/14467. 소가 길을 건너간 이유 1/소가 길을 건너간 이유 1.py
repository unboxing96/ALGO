t = int(input())

data = [-1] * (t + 1)
cnt = 0

for _ in range(t):
    a, b = map(int, input().split())
    
    if data[a] == -1:
        data[a] = b
    elif data[a] != b:
        data[a] = b
        cnt += 1

print(cnt)