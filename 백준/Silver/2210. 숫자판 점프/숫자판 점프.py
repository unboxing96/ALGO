def dfs(x, y, number):
    if len(number) == 6: 
        if number not in result: 
            result.append(number)
        return
        
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1] 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5: #범위 내에 있다면
            dfs(nx, ny, number + matrix[nx][ny]) #6글자가 될 때 까지 재귀

#입력
matrix = [list(map(str, input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j]) #0,0부터 4,4까지 모두 검사
print(len(result))

