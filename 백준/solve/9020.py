# 에라토스테네스의 체로 n 이하의 소수 구하고,
# BFS??로 최소 차 합 구하기


def is_prime(n):

    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a, b = n // 2, n // 2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
