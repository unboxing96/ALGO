def solution(sequence, k):

    result = []
    prefix = [0] * (len(sequence) + 1)

    for i in range(len(sequence)):
        prefix[i + 1] = prefix[i] + sequence[i]

    left = 0
    right = 1

    while left < right:

        if right > len(sequence):
            break

        tmp = prefix[right] - prefix[left]

        if tmp == k:
            result.append([left, right-1])
            right += 1

        elif tmp < k:
            right += 1

        elif tmp > k:
            left += 1

    answer = sorted(result, key=lambda k: (k[1] - k[0], k[0]))

    if len(answer) > 0:
        return answer[0]
    else:
        return None


sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5

print(solution(sequence, k))
