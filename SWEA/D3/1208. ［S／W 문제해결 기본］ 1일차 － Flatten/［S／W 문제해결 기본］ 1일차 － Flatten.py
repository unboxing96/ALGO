def my_max(iterable):
    max_num = iterable[0]
    for i in range(1, len(iterable)):
        if max_num < iterable[i]:
            max_num = iterable[i]
    return max_num

# TestCase만큼 반복
for tc in range(1, 10 + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    counts = [0] * (my_max(arr) + 1)
    for i in range(len(arr)):
        counts[arr[i]] += 1

    s = 0
    e = len(counts) - 1
    cnt = 0
    while s + 1 < e and cnt < n:
        if not counts[e]:
            e -= 1
            continue
        if not counts[s]:
            s += 1
            continue

        counts[e] -= 1
        counts[s] -= 1
        counts[s + 1] += 1
        counts[e - 1] += 1
        cnt += 1

    while counts[s] == 0: # 탐색 끝낸 뒤에, 가장 낮은 높이
        s += 1

    while counts[e] == 0: # 탐색 끝낸 뒤에, 가장 높은 높이
        e -= 1

    print(f'#{tc} {e - s}')