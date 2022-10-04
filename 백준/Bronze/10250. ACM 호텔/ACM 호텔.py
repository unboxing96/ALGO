T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())

    right = n // h + 1
    left = n % h

    if n % h == 0:
        right = n // h
        left = h

    print(f"{left * 100 + right}")
