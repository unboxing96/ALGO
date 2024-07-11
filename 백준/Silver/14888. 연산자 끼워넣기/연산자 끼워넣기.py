n = int(input())
numArr = list(map(int, input().split()))
opArr = list(map(int, input().split()))
maxNum = -int(1e9)
minNum = int(1e9)

def dfs(add, sub, mul, div, temp, i):
    global maxNum, minNum

    if i == n:
        maxNum = max(maxNum, temp)
        minNum = min(minNum, temp)
        return

    if add:
        dfs(add - 1, sub, mul, div, temp + numArr[i], i + 1)
    if sub:
        dfs(add, sub - 1, mul, div, temp - numArr[i], i + 1)
    if mul:
        dfs(add, sub, mul - 1, div, temp * numArr[i], i + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(temp / numArr[i]), i + 1)

dfs(opArr[0], opArr[1], opArr[2], opArr[3], numArr[0], 1)
print(maxNum)
print(minNum)