import sys

def eratos(n):
    sieve = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = 0

    return sum([1 for i in range(2, n + 1) if sieve[i] and i > n/2])


def solve(n):
    return eratos(2*n)


while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    print(solve(n))