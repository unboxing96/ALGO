n, m = map(int, input().split())
arr = ()
arrArr = set()

def dfs(arr):
    if len(arr) == m and arr not in arrArr:
        print(*arr, sep=" ")
        arrArr.add(tuple(arr))
        return

    for i in range(1, n + 1):
        dfs(arr + (i, ))

dfs(arr)