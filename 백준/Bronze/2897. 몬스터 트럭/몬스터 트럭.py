# 행, 열 값 받기
R, C = map(int, input().split()) # R: 행, C: 열

# 주차장 행렬 받기
matrix = []
for i in range(R):
    matrix.append(input())

# 정답 리스트
result = [0 for _ in range(5)]


# 델타 값 (순서: 원점, 우, 하, 우하)
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

for x in range(R-1): # 행
    for y in range(C-1): # 열
        
        isBool = True
        
        X_cnt = 0
        for i in range(4): # 델타

            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if matrix[nx][ny] == "#": 
                    isBool = False
                    break
                elif matrix[nx][ny] == "X":
                    X_cnt += 1
    
        if isBool == True:
            result[X_cnt] += 1

print(*result, sep="\n")