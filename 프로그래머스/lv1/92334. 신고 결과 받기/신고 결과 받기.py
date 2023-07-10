from collections import defaultdict

def solution(id_list, report, k):

    dict1 = defaultdict(set)
    dict2 = defaultdict(set)

    for rep in report:
        user, target = rep.split()
        dict1[user].add(target)
        dict2[target].add(user)

    result = []
    for user in id_list:
        tmp = 0
        for target in dict1[user]:
            if len(dict2[target]) >= k:
                tmp += 1
        result.append(tmp)

    return result