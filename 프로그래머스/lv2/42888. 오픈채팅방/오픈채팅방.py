
def solution(record):

    msg = []
    dic = {}

    for rec in record:
        # r= io, id, nick
        r = list(rec.split())

        if len(r) == 3:
            if r[0] == "Enter":
                dic[r[1]] = r[2]
                msg.append((r[0], r[1]))
            elif r[0] == "Change":
                dic[r[1]] = r[2]
        else:  # io == "Leave"
            msg.append((r[0], r[1]))

    result = []
    for m in msg:
        if m[0] == "Enter":
            result.append(f"{dic[m[1]]}님이 들어왔습니다.")
        else:
            result.append(f"{dic[m[1]]}님이 나갔습니다.")

    return result
