from collections import deque

# define the four possible movements (up, down, left, right)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# read the input
n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# find the location of the target
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            target_x, target_y = i, j

# initialize the distance matrix
dist = [[-1]*m for i in range(n)]

# breadth-first search starting from the target
queue = deque([(target_x, target_y)])
dist[target_x][target_y] = 0

while queue:
    curr_x, curr_y = queue.popleft()
    for i in range(4):
        next_x, next_y = curr_x + dx[i], curr_y + dy[i]
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if grid[next_x][next_y] == 0:
            continue
        if dist[next_x][next_y] != -1:
            continue
        dist[next_x][next_y] = dist[curr_x][curr_y] + 1
        queue.append((next_x, next_y))

# print the result
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print("0", end=" ")
        elif dist[i][j] == -1:
            print("-1", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
