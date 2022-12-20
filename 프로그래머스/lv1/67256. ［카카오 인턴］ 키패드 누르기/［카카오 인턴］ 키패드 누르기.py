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