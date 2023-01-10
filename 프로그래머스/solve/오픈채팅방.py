# Enter -> { 아이디 : 닉네임} 변경
# Change -> { 아이디 : 닉네임} 변경
# msg -> [["Enter", "아이디"], ["Leave", "아이디"], ...] 형식으로 append
# msg 반복하면서 딕셔너리[아이디] 출력


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


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]

print(solution(record))
