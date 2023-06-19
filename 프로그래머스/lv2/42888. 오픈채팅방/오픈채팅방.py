from collections import defaultdict

def solution(record):
    answer = []

    msg = []
    dic = defaultdict(str)

    for rec in record:

        order = list(rec.split())

        if order[0] == "Enter" or order[0] == "Leave":
            msg.append([order[0], order[1]])
        
        if order[0] == "Enter" or order[0] == "Change":
            dic[order[1]] = order[2]

    for m in msg:
        if m[0] == "Enter":
            answer.append(f"{dic[m[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{dic[m[1]]}님이 나갔습니다.")

    return answer
