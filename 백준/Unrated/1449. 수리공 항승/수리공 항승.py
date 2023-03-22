n, l = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

visited = [False] * (max(array) + l)

cnt = 0

for i in range(len(array)):
    now = array[i]
    if not visited[now]:
        for j in range(now, now + l):
            visited[j] = True
        
        cnt += 1

print(cnt)