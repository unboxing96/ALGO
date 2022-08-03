N = int(input())

# 행 * 렬 -> 열 * 행 바꾸기
matrix = [[], [], []]
sum = []

for _ in range(N):
    a, b, c = map(int, input().split())
    matrix[0].append(a)
    matrix[1].append(b)
    matrix[2].append(c)

for i in range(N): # 플레이어 5
    score = 0
    for j in range(3): # 게임 3
        if matrix[j].count(matrix[j][i]) == 1:
            score += matrix[j][i]
    sum.append(score)

for i in sum:
    print(i)