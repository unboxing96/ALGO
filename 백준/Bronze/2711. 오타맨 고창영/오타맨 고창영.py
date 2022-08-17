T = int(input())

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = list(B)
    del B[A - 1]
    result = "".join(B)
    print(result)