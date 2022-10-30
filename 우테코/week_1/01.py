from os import P_ALL


pobi = [99, 102]
crong = [211, 212]


def book(pobi, crong):

    # 예외 처리
    if pobi[1] - pobi[0] != 1:
        return -1
    elif crong[1] - crong[0] != 1:
        return -1

    # 왼쪽, 오른쪽 나눠서 구함
    # 문자열 변환 후 반복하며, 덧셈 // 곱셈 후 결과 각각 append

    pobi_list = []

    for i in range(2):  # 왼쪽 오른쪽

        tmp_sum = 0
        tmp_mul = 1

        for j in str(pobi[i]):  # pobi[0]을 반복 -> "9", "7"

            j = int(j)

            tmp_sum += j
            tmp_mul *= j

        pobi_list.append(tmp_sum)
        pobi_list.append(tmp_mul)

    crong_list = []

    for i in range(2):  # 왼쪽 오른쪽

        tmp_sum = 0
        tmp_mul = 1

        for j in str(crong[i]):  # pobi[0]을 반복 -> "9", "7"

            j = int(j)

            tmp_sum += j
            tmp_mul *= j

        crong_list.append(tmp_sum)
        crong_list.append(tmp_mul)

    mp = max(pobi_list)
    mc = max(crong_list)

    if mp > mc:
        return 1
    elif mp < mc:
        return 2
    elif mp == mc:
        return 0


result = book(pobi, crong)
print(result)
