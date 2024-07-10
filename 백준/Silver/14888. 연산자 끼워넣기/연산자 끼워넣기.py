n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 덧, 뺄, 곱, 나
maxNum = - int(1e9)
minNum = int(1e9)

def dfs(add, sub, mul, div, sum, idx):
    global maxNum, minNum

    if idx == n:
        maxNum = max(maxNum, sum)
        minNum = min(minNum, sum)
        return

    if add:
        dfs(add - 1, sub, mul, div, sum + arr[idx], idx + 1)
    if sub:
        dfs(add, sub - 1, mul, div, sum - arr[idx], idx + 1)
    if mul:
        dfs(add, sub, mul - 1, div, sum * arr[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(sum / arr[idx]), idx + 1)

dfs(add, sub, mul, div, arr[0], 1)
print(maxNum)
print(minNum)