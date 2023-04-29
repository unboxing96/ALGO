
n, m = map(int, input().split())

듣도 = set()
보도 = set()

for _ in range(n):
    듣도.add(input())

for _ in range(m):
    보도.add(input())

result = sorted(list(듣도 & 보도))

print(len(result))
print(*result, sep="\n")