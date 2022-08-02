N = int(input())
result = []
for i in range(N):
    r, e, c = map(int, input().split())
    if r > (e - c):
        result.append("do not advertise")
    elif r < (e - c):
        result.append("advertise")
    elif r == (e - c):
        result.append("does not matter")

print('\n'.join(result))