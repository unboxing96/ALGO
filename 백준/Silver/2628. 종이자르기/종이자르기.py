m, n = map(int, input().split())
tc = int(input())
matrix = [[0] * m for _ in range(n)]
count_dict = {}

for _ in range(tc):
    dir, index = map(int, input().split())

    if dir == 0: # 가로
        for i in range(index):
            for j in range(m):
                matrix[i][j] += 1
    
    elif dir == 1:
        for i in range(n):
            for j in range(index):
                matrix[i][j] += 100

for i in range(n):
    for j in range(m):
        if count_dict.get(matrix[i][j], 0):
            count_dict[matrix[i][j]] += 1
        else:
            count_dict[matrix[i][j]] = 1

max_value = 0
for k, v in count_dict.items():
    if max_value < v:
        max_value = v

print(max_value)