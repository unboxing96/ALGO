n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(sum([sum(arr[a][j-1:y]) for a in range(i-1, x)]))