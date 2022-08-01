from collections import deque


N = int(input())

num_li = []

for i in range(1, N+1):
    num_li.append(i)

dq = deque(num_li)



result = []
while len(dq) > 1:
    result.append(dq.popleft())
    dq.append(dq.popleft())

print(*result, *dq)