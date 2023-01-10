# k진수로 나타내기
# n을 k 제곱의 범위로 나타내기: k^m <= n <= k^m+1
# 길이가 m+1인 배열로 표시하기 (0으로 초기화): [k^m, k^m-1, k^m-2 ... k^2, k^1, k^0]
# for문 반복하며, n값을 k진수로 배열에 표시
# 배열을 문자열로 전환
# 문자열을 0으로 나눔: map(int, split("0"))
# 가장 큰 수보다 작은 소수 리스트를 구함
# 소수 개수 구하기


# def solution(n, k):

#     # n을 k 제곱의 범위로 나타내기: k^m <= n <= k^m+1
#     m = 0
#     while True:
#         if k**m >= n:
#             m -= 1
#             break
#         m += 1

#     # 길이가 m+1인 배열로 표시하기 (0으로 초기화): [k^m, k^m-1, k^m-2 ... k^2, k^1, k^0]
#     jinsoo = [0] * (m + 1)

#     for i in range(len(jinsoo)):
#         up = k ** (m - i)
#         for j in range(k - 1):
#             if n >= up:
#                 n -= up
#                 jinsoo[i] += 1

#     # 배열을 문자열로 전환
#     jinsoo = "".join(str(i) for i in jinsoo)

#     # 문자열을 0으로 나눔: map(int, split("0"))
#     jinsoo = jinsoo.split("0")

#     # 0으로 나눈 int 리스트
#     data = []
#     for i in jinsoo:
#         if i:
#             data.append(int(i))

#     # 가장 큰 수보다 작은 소수 리스트를 구함
#     result = []
#     for d in data:
#         if d == 1:
#             continue
#         for i in range(2, int(d**0.5) + 1):
#             if d % i == 0:
#                 break
#         else:
#             result.append(d)

#     return len(result)


# n을 k진법으로 나타낸 문자열 반환
def solution(n, k):
    s = ""
    while n:
        s += str(n % k)
        n //= k
    return s[::-1]


n = 437674
k = 3
print(solution(n, k))
