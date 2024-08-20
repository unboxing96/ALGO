n, m = map(int, input().split())

def dfs(arr):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            if not arr or arr[-1] < i:
                visited[i] = True
                dfs(arr + [i])
                visited[i] = False

arr = []
visited = [False] * (n + 1)

dfs(arr)