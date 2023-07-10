def solution(want, number, discount):   

    result = 0

    for i in range(len(discount) + 1 - 10):
        tmp_arr = discount[i:i+10]
        tmp_dict = {}
        for tmp in tmp_arr:
            if tmp in tmp_dict:
                tmp_dict[tmp] += 1
            else:
                tmp_dict[tmp] = 1

        tmp = 0
        for w in want:
            if w in tmp_dict:
                if tmp_dict[w] >= number[want.index(w)]:
                    tmp += 1

            if tmp == len(want):
                result += 1

    return result