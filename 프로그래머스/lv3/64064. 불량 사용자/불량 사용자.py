import re
from itertools import permutations


def solution(user_id, banned_id):

    answer = set()
    n = len(banned_id)
    perm = list(permutations(user_id, n))

    for p in perm:
        cnt = 0
        for i in range(n):
            # 필터링한 아이디와 특정 조합 내 원소인 아이디가 매치되지 않거나, 매치된 부분의 길이가 다를경우 (동일한 문자가 아닐 경우) -> break
            if not re.match(banned_id[i].replace("*", "."), p[i]) or len(
                banned_id[i]
            ) != len(p[i]):
                break
            else:
                cnt += 1

        if cnt == n:
            answer.add(frozenset(p))

    return len(answer)