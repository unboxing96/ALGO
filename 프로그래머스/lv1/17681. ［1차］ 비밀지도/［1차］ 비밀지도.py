def solution(n, arr1, arr2):

    result = []
    for i in range(n):
        new = bin(arr1[i] | arr2[i])[2:].rjust(n, "0")
        new = new.replace("1", "#")
        result.append(new.replace("0", " "))

    return result
