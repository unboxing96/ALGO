def solution(today, terms, privacies):

    # 오늘 날짜 파싱
    ty, tm, td = map(int, today.split("."))

    # 약관 파싱
    t_dic = {}
    for t in terms:
        a, b = t.split()
        t_dic[a] = int(b)

    # 개인정보 파싱
    p_dic = {}
    for i, p in enumerate(privacies):
        date, name = p.split()
        ny, nm, nd = map(int, date.split("."))
        p_dic[i + 1] = [ny, nm, nd, name]

    result = []
    for p in p_dic:

        isBool = False

        py, pm, pd = p_dic[p][0], p_dic[p][1], p_dic[p][2]

        # 약관 더하기
        pm += t_dic[p_dic[p][3]]
        # 12월 넘어가면 처리

        while True:
            if pm <= 12:
                break
            py += pm // 12
            pm %= 12

            if pm == 0:
                pm = 12
                py -= 1

        if py < ty:
            isBool = True

        elif py == ty:
            if pm < tm:
                isBool = True

            elif pm == tm:
                if pd <= td:
                    isBool = True

        if isBool:
            result.append(p)

    return result


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = [
    "2019.01.01 D",
    "2019.11.15 Z",
    "2019.08.02 D",
    "2019.07.01 D",
    "2018.12.28 Z",
]

print(solution(today, terms, privacies))
