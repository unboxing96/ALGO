# stack 2개 생성
# str1, str2을 반복하며 temp에 문자열만 2개 추가
# temp 길이가 2가 되면 각 stack에 추가
# 중복 집합
# 중복 교집합:
# # stack 하나를 반복하면서 있으면 양쪽에서 pop(), 교집합 리스트에 추가
# 중복 합집합;
# # stack 두개를 반복하면서, 있거나 없거나 양쪽에서 pop(), 합집합 리스트에 추가
# 자카드 유사도 계산

from collections import Counter


def solution(str1, str2):

    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []

    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for j in range(len(str2_low) - 1):
        if str2_low[j].isalpha() and str2_low[j + 1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j + 1])

    c1 = Counter(str1_lst)
    c2 = Counter(str2_lst)

    inter = list((c1 & c2).elements())
    union = list((c1 | c2).elements())

    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)


str1 = "handshake"
str2 = "shake hands"
print(solution(str1, str2))
