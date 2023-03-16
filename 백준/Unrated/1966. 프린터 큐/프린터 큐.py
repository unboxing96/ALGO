from collections import deque

n = int(input())

for _ in range(n):
    size, goal = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        MAX = max(q)
        first = q.popleft()
        goal -= 1

        if MAX == first:
            cnt += 1
            if goal < 0:
                print(cnt)
                break
        else:
            q.append(first)
            if goal < 0:
                goal = len(q) - 1