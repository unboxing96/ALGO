import sys
sys.stdin = open("음료수얼려먹기.txt", "r")

# 모든 요소를 탐색해야 하므로, DFS든 BFS든 상관 없다.
# 값이 0인 부분이 "있다"고 보는 것이다.
# 전체 배열을 탐색하면서, 0을 만나면 DFS를 진행하고, DFS가 종료될 때마다 count += 1, count를 return하면 된다.
# 4방향 탐색을 해야 한다.

r, c = map(int, input().split())
graph = [list(map(int, input())) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

def dfs(x, y):
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    
    if graph[x][y] == 0: # 아직 방문하지 않은 노드라면
        graph[x][y] = 1 # 방문 처리를 하고

        for i in range(4): # 4방향 DFS
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        
        return True # 탐색이 성공적으로 끝나면 True
    
    # 반환값이 지정되지 않았을 경우 return None (추가적인 동작 없이 종료)
    # return False를 해주는 것이 좋다.
    

for i in range(r):
    for j in range(c):
        if graph[i][j] == 0:
            if dfs(i, j) == True:
                cnt += 1

print(cnt)