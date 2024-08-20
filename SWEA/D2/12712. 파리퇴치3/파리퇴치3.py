def hitPlus(n, m, x, y, arr):
    tempCount = 0
    for i in range(x-m+1, x+m):
        for j in range(y-m+1, y+m):
            if i < 0 or i >= n or j < 0 or j >= n:
                continue
            if i == x or j == y:
                tempCount += arr[i][j]
    return tempCount

def hitX(n, m, x, y, arr):
    tempCount = 0
    for i in range(x-m+1, x+m):
        for j in range(y-m+1, y+m):
            if i < 0 or i >= n or j < 0 or j >= n:
                continue
            if i + j == x + y or i - j == x - y:
                tempCount += arr[i][j]
    return tempCount

testCase = int(input())
for tc in range(testCase):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for x in range(n):
        for y in range(n):
            plusResult = hitPlus(n, m, x, y, arr)
            xResult = hitX(n, m, x, y, arr)
            result = max(result, plusResult, xResult)

    print(f"#{tc+1} {result}")