N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

K = int(input())

for i in range(K): # 3번 반복
    i, j, x, y = map(int, input().split())

    sum = 0
    for a in range(min(i, x)-1, max(i, x)):
        for b in range(min(j, y)-1, max(j, y)):
            sum += matrix[a][b]
    print(sum)
    