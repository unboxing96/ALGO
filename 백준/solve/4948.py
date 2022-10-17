def prime(n):
    nums = [True] * (n + 1)

    for i in range(2, int(n**0.5) + 1):
        if nums[i] == True:
            for j in range(i + i, n + 1, i):
                nums[i] = False

    return sum([i for i in range(2, n + 1) if nums[i] == True] and i > n / 2)


def solve(n):
    return prime(2 * n)


while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
