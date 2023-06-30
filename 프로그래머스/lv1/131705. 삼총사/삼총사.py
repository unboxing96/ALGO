def solution(number):

    arr_size = len(number)
    result = 0

    for i in range(arr_size):
        for j in range(i+1, arr_size):
            for k in range(j+1, arr_size):
                if number[i] + number[j] + number[k] == 0:
                    result += 1

    return result