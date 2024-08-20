from collections import deque
import copy

def find_closest_fish(sx, sy):
    visited = [[False] * n for _ in range(n)]
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    fishes = []

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if matrix[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if 0 < matrix[nx][ny] < shark_size:  # 먹을 수 있는 물고기 발견
                        fishes.append((dist + 1, nx, ny))
                    else:  # 빈 칸 또는 같은 크기의 물고기
                        q.append((nx, ny, dist + 1))

    if fishes:
        # 거리가 가장 가까운, 가장 위쪽, 가장 왼쪽 물고기를 선택
        fishes.sort()
        return fishes[0]
    else:
        return [0, 0, 0]  # 더 이상 먹을 물고기가 없을 때

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
shark_size = 2
shark_exp = 0
sx = 0
sy = 0
result = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            sx = i
            sy = j
            matrix[i][j] = 0  # 상어의 위치를 0으로 초기화

while True:
    dist, next_fish_x, next_fish_y = find_closest_fish(sx, sy)

    if dist:
        sx = next_fish_x
        sy = next_fish_y
        matrix[sx][sy] = 0  # 물고기를 먹은 위치를 0으로 초기화

        shark_exp += 1
        if shark_exp == shark_size:
            shark_size += 1
            shark_exp = 0
        
        result += dist
    
    else:
        break

print(result)
