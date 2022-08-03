N, M = map(int, input().split())

matrix = [] # [['....'], ['....'], ['....'], ['....']]
for i in range(N):
    matrix.append(list(input().split()))

# print(matrix, "matrix")

set_X = set()
set_Y = set()

for j in range(len(matrix)): # mat = ['XX...']의 형태이므로
    line = matrix[j][0] # matrix[j] = ['XX...'], matrix[j]0] = 'XX...'
    
    for k in range(len(line)):
        if "X" == line[k]:
            # print(j, k)
            set_X.add(j) # 행
            set_Y.add(k) # 열
    
# print(set_X, "set_X")
# print(set_Y, "set_Y")

result = [N - len(set_X), M - len(set_Y)] # 최소 채워야 하는 행 개수, 열 개수

if max(result):
    print(max(result))
else:
    print(0)