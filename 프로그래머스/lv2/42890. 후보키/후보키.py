
from itertools import combinations as combi


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combi(range(col), i))

    # print(candidates)

    # 유일성
    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candi)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if set(unique[i]) == set(unique[i]) & set(unique[j]):
                answer.discard(unique[j])

    return len(answer)
