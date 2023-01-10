# k를 n진법으로 표현하기
# # k가 0이 될 때까지
# # k를 n으로 나눈 나머지를 빈 문자열에 붙이고
# # k를 n으로 나눠줌
# # 문자열[::-1]

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


n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))
