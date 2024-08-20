n, m = map(int, input().split())
arr = []

def dfs(arr):
    if len(arr) == m:
        print(*arr, sep=" ")
        return

    for i in range(1, n + 1):
        if not arr or arr[-1] <= i:
            dfs(arr + [i])

dfs(arr)