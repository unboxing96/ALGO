# 각 손가락의 현재 위치를 저장한다.
# 다음 위치를 받는다.
# if 1, 4, 7 -> 왼손
# elif 3, 6, 9 -> 오른손
# else: 각 손가락의 다음 위치까지의 거리를 저장한다.
# -> 거리는, {번호 : 좌표} 딕셔너리를 생성하여, 좌표끼리 뺄셈으로 구함.
# 거리가 같다면 주 손에 따라
# 거리가 다르다면 가까운 손으로


def solution(numbers, hand):

    keypad = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        "*": [0, 3],
        0: [1, 3],
        "#": [2, 3],
    }

    l_now = "*"
    r_now = "#"

    route = []

    for i in range(len(numbers)):
        if str(numbers[i]) in "147":
            l_now = numbers[i]
            route.append("L")
        elif str(numbers[i]) in "369":
            r_now = numbers[i]
            route.append("R")
        else:  # numbers[i] in 2580
            l_calc = abs((keypad[numbers[i]][0]) - keypad[l_now][0]) + abs(
                (keypad[numbers[i]][1] - keypad[l_now][1])
            )
            r_calc = abs((keypad[numbers[i]][0] - keypad[r_now][0])) + abs(
                keypad[numbers[i]][1] - keypad[r_now][1]
            )

            if l_calc < r_calc:
                l_now = numbers[i]
                route.append("L")
            elif r_calc < l_calc:
                r_now = numbers[i]
                route.append("R")
            else:  # l_calc == r_calc
                if hand == "left":
                    l_now = numbers[i]
                    route.append("L")
                elif hand == "right":
                    r_now = numbers[i]
                    route.append("R")

    answer = "".join(route)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
