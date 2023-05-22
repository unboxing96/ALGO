
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

i = 0
j = n - 1

answer_sum = abs(num_list[i] + num_list[j])
answer_list = [num_list[i], num_list[j]]


while i < j:
    left = num_list[i]
    right = num_list[j]
    tmp_sum = left + right

    if abs(tmp_sum) < answer_sum:
        answer_sum = abs(tmp_sum)
        answer_list = [left, right]

        if answer_sum == 0:
            break

    if tmp_sum < 0:
        i += 1
    else:
        j -= 1

print(*answer_list)