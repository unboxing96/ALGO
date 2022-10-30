from collections import defaultdict


def algo(user, friends, visitors):

    dict = {}
    dict = defaultdict(list)  # 뮨자열 비었으면, 빈 리스트 생성

    for friend in friends:
        dict[friend[0]].append(friend[1])
        dict[friend[1]].append(friend[0])

    score = {}

    for k, v_list in dict.items():

        if k != user:
            for v in v_list:
                if v in dict[user]:
                    score[k] = score.get(k, 0) + 5

    for visitor in visitors:
        score[visitor] = score.get(visitor, 0) + 1

    score = sorted(score.items(), key=lambda x: x[1], reverse=True)

    result = []
    for name in score[:5]:
        if name[1] > 1:
            result.append(name[0])

    return result


user = "mrko"
friends = [
    ["donut", "andole"],
    ["donut", "jun"],
    ["donut", "mrko"],
    ["shakevan", "andole"],
    ["shakevan", "jun"],
    ["shakevan", "mrko"],
]
visitors = ["bedi", "bedi", "donut", "bedi", "shakevan"]

result = algo(user, friends, visitors)
print(result)
