n = int(input())
rope = [int(input()) for i in range(n)]

rope.sort(reverse=True)

ans = []
for i in range(n):
    ans.append(rope[i] * (i + 1))

print(max(ans))
