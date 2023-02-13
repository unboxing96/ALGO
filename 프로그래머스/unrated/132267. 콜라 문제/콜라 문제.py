def solution(a, b, n):

    tot = 0

    while n >= a:
        반환 = (n // a) * b
        나머지 = n % a

        tot += 반환
        n = 반환 + 나머지

    return tot