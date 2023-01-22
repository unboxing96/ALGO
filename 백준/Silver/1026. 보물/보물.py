n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

tot = 0
for i in range(n):
    tot += (A[i] * B[i])

print(tot)