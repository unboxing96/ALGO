# 각 배열에서 하나씩 꺼내서 2진수로 변환
# 변환된 2진수 2개를 or 연산
# 나온 값을, 1은 "#"으로, 0은 " "으로 변경
# 리스트에 저장
# 하나씩 출력


def solution(n, arr1, arr2):

    answer = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])[2:]
        temp = temp.rjust(n, "0")
        for r in (("1", "#"), ("0", " ")):
            temp = temp.replace(*r)
        answer.append(temp)
    return answer


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))
