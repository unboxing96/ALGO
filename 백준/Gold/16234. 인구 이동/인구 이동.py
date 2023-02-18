from collections import deque

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

def bfs(start, visited):
    queue = deque([start])
    union = [start]
    total_population = countries[start[0]][start[1]]

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) in visited:
                continue
            population_diff = abs(countries[x][y] - countries[nx][ny])
            if l <= population_diff <= r:
                visited.add((nx, ny))
                queue.append((nx, ny))
                union.append((nx, ny))
                total_population += countries[nx][ny]
    return union, total_population

days = 0
while True:
    visited = set()
    unions = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                visited.add((i, j))
                union, total_population = bfs((i, j), visited)
                if len(union) > 1:
                    unions.append((union, total_population))

    if not unions:
        break

    for union, total_population in unions:
        population_per_country = total_population // len(union)
        for x, y in union:
            countries[x][y] = population_per_country
    days += 1

print(days)
