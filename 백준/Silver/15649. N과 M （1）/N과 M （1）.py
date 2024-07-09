def backTracking(arr):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            backTracking(arr + [i])
            visited[i] = False

n, m = map(int, input().split())
arr = []
visited = [False] * (n + 1)

backTracking(arr)