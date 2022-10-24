N, K = map(int, input().split())

data = []
for i in range(1, N+1):
    if N % i == 0:
        data.append(i)

if K > len(data):
    print("0")
else:
    print(data[K-1])