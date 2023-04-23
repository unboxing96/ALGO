N = int(input())
M = int(input())

arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = -1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][k] == arr[k][j] and arr[i][k] != 0:
                arr[i][j] = arr[i][k]

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if arr[i][j] == 0:
            cnt += 1
    print(cnt - 1)

    
  