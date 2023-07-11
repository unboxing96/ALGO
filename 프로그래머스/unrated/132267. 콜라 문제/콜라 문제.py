def solution(a, b, n):

    tot = 0

    while n >= a:
        recycle = (n // a) * b
        leftover = n % a

        tot += recycle
        n = recycle + leftover

    return tot