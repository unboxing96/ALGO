import sys
from itertools import permutations

sys.stdin = open("2309.txt", "r")

# 리스트로 입력받기
numbers = []
for tc in range(9):
    numbers.append(int(input()))

# 오름차순 정렬
numbers.sort()

# 일곱 난쟁이 키의 모든 조합
answer_list = list(permutations(numbers, 7))

# 조합 중에 합이 100이 되는 조합 출력
for case in answer_list:
    if sum(case) == 100:
        print(*case, sep="\n")
        break


#################################


# 리스트로 입력받기
numbers = []
for tc in range(9):
    numbers.append(int(input()))

# 리스트의 합을 구해서 2명을 뺀 값이 100이 되는지 (7중 반복문 대신 2중 반복문)
sum_ = sum(numbers)

# 돌면서 뺀 값이 100이 되면, 2개 값 따로 저장
for i in range(len(numbers)):
    for j in range(1, len(numbers)):
        if sum_ - numbers[i] - numbers[j] == 100:
            a = numbers[i]
            b = numbers[j]

# 돌면서, 위에서 저장한 2개 값이 아니면 출력
for num in numbers:
    if num == a or num == b:
        pass
    else:
        print(num)
