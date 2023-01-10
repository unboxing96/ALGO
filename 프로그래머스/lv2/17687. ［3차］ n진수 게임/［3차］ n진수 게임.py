# 16진법 표기
hex = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

# n진법, k
def transfer(n, k):
    # 0 예외 처리
    if k == 0:
        return 0

    s = ""
    while k:
        s += hex.get(k % n, str(k % n))
        k //= n
    return s[::-1]


def solution(n, t, m, p):
    loop = ""
    k = t * m
    for i in range(k + 1):
        loop += str(transfer(n, i))

    result = ""
    for j in range(p - 1, len(loop), m):
        result += loop[j]

    return result[:t]