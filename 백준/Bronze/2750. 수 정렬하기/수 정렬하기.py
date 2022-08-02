N = int(input())
result = []
for _ in range(N):
    result.append(int(input()))

result.sort()
for i in result:
    print(i)