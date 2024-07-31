######################################
# sum
def my_sum(iterable, start=0):
    for elem in iterable:
        start += elem
    return start

# max
def my_max(iterable):
    max_value = iterable[0]
    for i in range(1, len(iterable)):
        if max_value < iterable[i]:
            max_value = iterable[i]
    return max_value
######################################

# TestCase 개수
T = 10

# TestCase만큼 반복
for _ in range(T):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    right_diagonal = []
    left_diagonal = []
    horizontal = [[] for _ in range(100)]
    vertical = [[] for _ in range(100)]

    for i in range(100):
        for j in range(100):
            horizontal[i].append(matrix[i][j])
            vertical[j].append(matrix[i][j])
            if i == j:
                right_diagonal.append(matrix[i][j])
            if i + j == 99:
                left_diagonal.append(matrix[i][j])

    max_horizontal = my_max(list(map(sum, horizontal)))
    max_vertical =  my_max(list(map(sum, vertical)))
    max_right_diagonal = my_sum(right_diagonal)
    max_left_diagonal = my_sum(left_diagonal)
    result = my_max([max_horizontal, max_vertical, max_right_diagonal, max_left_diagonal])

    print(f'#{tc} {result}')

