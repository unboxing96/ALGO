import sys

sys.stdin = open("3085.txt", "r")

n = int(input())

data = []
for _ in range(n):
    data.append(input())

print(data[0])
print(data[0][1])
