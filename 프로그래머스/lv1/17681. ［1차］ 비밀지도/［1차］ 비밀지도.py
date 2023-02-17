def solution(n, arr1, arr2):

    new = []
    for i in range(n):
        new.append(arr1[i] | arr2[i])

    last = []
    for i in range(n):
        last.append(bin(new[i])[2:].rjust(n, "0"))

    result = []
    for i in range(n):
        res = last[i].replace("1", "#")
        res = res.replace("0", " ")
        result.append(res)

    return result