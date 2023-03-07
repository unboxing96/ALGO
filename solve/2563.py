import sys
sys.stdin = open("2563.txt", "r")

# count all 1
# subtract all >= 2

n = int(input()) # number of page
graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    y, x = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            graph[i][j] += 1

all_cnt = 0

for i in range(101):
    for j in range(101):
        if graph[i][j] >= 1:
            all_cnt += 1

print(all_cnt)
