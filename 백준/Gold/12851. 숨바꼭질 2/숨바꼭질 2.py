from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
fast, way = 1e9, 0
q = deque([(n, 0)])

while q:
    idx, time = q.popleft()
    visited[idx] = True

    if idx == k and time <= fast:
        fast = min(fast, time)
        way += 1
    
    if time > fast:
        break

    for x in (idx - 1, idx + 1, idx * 2):
        if x in range(100001) and not visited[x]:
            q.append((x, time + 1))

print(fast)
print(way)