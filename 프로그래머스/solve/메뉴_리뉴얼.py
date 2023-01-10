# set 써서 orders 모든 조합 구함
# order = {1번 사람 : [모든 조합...]}
# order 반복하며 -> cnt = {조합 : cnt 횟수}
# order 반복하며 -> man = {조합 : 사람 cnt}

# course 반복하며 -> cnt 반복하며 course 개수 충족 + man 2 이상 충족 -> result에 append
# result sort 해서 출력

from itertools import combinations


def solution(orders, course):

    order = {}
    cnt = {}
    man_cnt = {}

    for i in range(len(orders)):
        comb = set(combinations(orders[i], 2))
        order[i + 1] = comb

    for o in order: # 한 명 딕셔너리
        for oo in order[o]: # 딕셔너리의 모든 조합 반복
            cnt.get(oo, 0) + 1

    return True


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

print(solution(orders, course))
