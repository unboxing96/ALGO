import sys
sys.stdin = open("12865.txt", "r")

n, k = map(int, input().split())

now_w = 0
now_v = 0

graph = [] # [[6, 13], [4, 8], [3, 6], [5, 12]]
for _ in range(n):
    graph.append(list(map(int, input().split())))

i = 0
cnt = 1
now = 0
result = []
def perm(graph, cnt):
    now += 1
    for i in range(i, len(graph)):
        if now == cnt:
            result.append(graph[i])
        else:
            