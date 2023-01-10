from itertools import combinations
from collections import Counter


def solution(orders, course):

    result = []

    for c in course:

        candidates = []
        cnt = {}

        for i in range(len(orders)):
            comb = combinations(orders[i], c)
            for com in comb:
                res = "".join(sorted(com))
                candidates.append(res)

        cand_cnt = Counter(candidates).most_common()

        for k, v in cand_cnt:
            if 2 <= v and v == cand_cnt[0][1]:
                result.append(k)

    return sorted(result)
