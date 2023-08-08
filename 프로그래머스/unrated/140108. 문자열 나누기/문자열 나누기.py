def solution(s):
    answer = 0
    cnt_same, cnt_diff = 0, 0
    x = ""

    for now_str in s:
        if x == "":
            x = now_str
            cnt_same += 1
        else:
            if x == now_str:
                cnt_same += 1
            else:
                cnt_diff += 1
            
            if cnt_same == cnt_diff:
                answer += 1
                x = ""
                cnt_same, cnt_diff = 0, 0

    # 남아있는 게 있으면 추가
    if cnt_same or cnt_diff:
        answer += 1

    return answer