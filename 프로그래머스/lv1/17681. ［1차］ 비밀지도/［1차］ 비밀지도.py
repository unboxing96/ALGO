
def solution(n, arr1, arr2):

    answer = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])[2:]
        temp = temp.rjust(n, "0")
        for r in (("1", "#"), ("0", " ")):
            temp = temp.replace(*r)
        answer.append(temp)
    return answer
